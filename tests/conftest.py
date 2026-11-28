"""Suite-wide test configuration.

The whole test session runs with network access blocked (docs/adr/0001-offline-at-runtime.md).
The guard is a Python audit hook. It is installed when this file is imported, which is
before any test module, and therefore before the package under test, is imported. Code
that reaches for the network while it is merely being imported is caught as well.

Audit hooks see socket use at the interpreter level, so the guard also covers code that
bypasses the ``socket`` module's Python wrappers. It does not see sockets opened by
native extensions that do not go through the interpreter; that risk is handled by
reviewing dependencies, not by this guard.
"""

import os
import sys
from collections.abc import Generator

import pytest
from hypothesis import settings

_EXPECTED_MARKER = "expects_blocked_network"

# Creating a socket, connecting, sending and every form of name resolution.
# ``socket.gethostname`` is deliberately absent: it reads the local host name and does
# not touch the network.
_BLOCKED_EVENTS = frozenset(
    {
        "socket.__new__",
        "socket.bind",
        "socket.connect",
        "socket.getaddrinfo",
        "socket.gethostbyaddr",
        "socket.gethostbyname",
        "socket.getnameinfo",
        "socket.sendmsg",
        "socket.sendto",
    }
)

_attempts: list[str] = []


class NetworkAccessBlockedError(RuntimeError):
    """Raised when code under test tries to use the network.

    Deliberately not an ``OSError``: libraries routinely catch ``OSError`` around
    network calls and fall back to something else, which would hide the attempt.
    """


def _network_guard(event: str, args: tuple[object, ...]) -> None:
    if event in _BLOCKED_EVENTS:
        _attempts.append(event)
        raise NetworkAccessBlockedError(f"network access is blocked in tests (audit event {event})")


# Audit hooks cannot be removed again. That is intended: nothing in this process may
# switch the guard off.
sys.addaudithook(_network_guard)


def pytest_collection_finish(session: pytest.Session) -> None:
    """Fail the run if importing the test modules already touched the network."""
    if _attempts:
        raise pytest.UsageError(
            f"network access was attempted while test modules were imported: {_attempts}"
        )


@pytest.hookimpl(wrapper=True)
def pytest_runtest_call(item: pytest.Item) -> Generator[None, object, object]:
    """Fail a test whose code tried the network, even if that code swallowed the error."""
    seen = len(_attempts)
    result = yield
    attempts = _attempts[seen:]
    if attempts and item.get_closest_marker(_EXPECTED_MARKER) is None:
        pytest.fail(f"code under test attempted network access: {attempts}", pytrace=False)
    return result


# Property tests explore at random on a developer machine and run from a fixed seed in
# CI, so that a CI failure is reproducible and never a matter of luck.
settings.register_profile("deterministic", derandomize=True, deadline=None, database=None)
if os.environ.get("CI"):
    settings.load_profile("deterministic")
