"""Command-line entry point.

This is the scaffold: the program can report its version and explain itself, nothing
more. The ``scan`` command arrives with the first-scan milestone.
"""

import argparse
from collections.abc import Sequence

from logai_scan import __version__
from logai_scan.names import COMMAND_NAME, PROJECT_NAME

_DESCRIPTION = (
    f"{PROJECT_NAME} analyses log exports locally and shows which AI services were "
    "reached from a network. It never accesses the network itself."
)
_EPILOG = "Pre-alpha scaffold: there are no commands yet."


def build_parser() -> argparse.ArgumentParser:
    """Return the argument parser of the command-line program."""
    parser = argparse.ArgumentParser(
        prog=COMMAND_NAME,
        description=_DESCRIPTION,
        epilog=_EPILOG,
        allow_abbrev=False,
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"{COMMAND_NAME} {__version__}",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the command-line program and return its exit status.

    ``argparse`` ends the process itself for ``--help``, ``--version`` (status 0) and
    for usage errors (status 2) by raising ``SystemExit``.
    """
    parser = build_parser()
    parser.parse_args(argv)
    parser.print_help()
    return 0
