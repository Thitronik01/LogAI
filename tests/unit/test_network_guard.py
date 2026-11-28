"""The test suite must not be able to reach the network (ADR 0001)."""

import socket
import urllib.request
from pathlib import Path

import pytest

BLOCKED = "network access is blocked"
CONFTEST = Path(__file__).resolve().parents[1] / "conftest.py"


@pytest.mark.expects_blocked_network
def test_creating_a_socket_is_blocked() -> None:
    with pytest.raises(RuntimeError, match=BLOCKED):
        socket.socket()


@pytest.mark.expects_blocked_network
def test_name_resolution_is_blocked() -> None:
    with pytest.raises(RuntimeError, match=BLOCKED):
        socket.getaddrinfo("service.test", 443)
    with pytest.raises(RuntimeError, match=BLOCKED):
        socket.gethostbyname("service.test")


@pytest.mark.expects_blocked_network
def test_high_level_clients_are_blocked() -> None:
    # 192.0.2.0/24 is reserved for documentation (RFC 5737); nothing is ever sent.
    with pytest.raises(RuntimeError, match=BLOCKED):
        urllib.request.urlopen("http://192.0.2.1/", timeout=1)


def test_reading_the_local_host_name_stays_possible() -> None:
    assert isinstance(socket.gethostname(), str)


def test_a_swallowed_attempt_still_fails_the_test(
    pytester: pytest.Pytester, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Code that catches the guard's error must not get away with the attempt."""
    # The inner run prints paths. On Windows a piped child process would encode them in
    # the ANSI code page, which breaks as soon as a path contains a non-ASCII character.
    monkeypatch.setenv("PYTHONIOENCODING", "utf-8")
    pytester.makeconftest(CONFTEST.read_text(encoding="utf-8"))
    pytester.makepyfile(
        """
        import contextlib
        import socket


        def test_swallows_the_error():
            with contextlib.suppress(Exception):
                socket.socket()


        def test_leaves_the_network_alone():
            assert True
        """
    )

    result = pytester.runpytest_subprocess()

    result.assert_outcomes(passed=1, failed=1)
    result.stdout.fnmatch_lines(["*code under test attempted network access*"])
