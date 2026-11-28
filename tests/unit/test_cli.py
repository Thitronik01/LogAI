"""Behaviour of the command-line scaffold."""

import pytest

from logai_scan import __version__
from logai_scan.cli import main
from logai_scan.names import COMMAND_NAME


def test_version_flag_prints_command_name_and_version(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as raised:
        main(["--version"])

    assert raised.value.code == 0
    assert capsys.readouterr().out.strip() == f"{COMMAND_NAME} {__version__}"


def test_version_comes_from_the_installed_distribution() -> None:
    assert __version__ != "0+unknown"


def test_without_arguments_the_help_text_is_shown(capsys: pytest.CaptureFixture[str]) -> None:
    assert main([]) == 0

    out = capsys.readouterr().out
    assert out.startswith(f"usage: {COMMAND_NAME}")
    assert "never accesses the network" in out


def test_an_unknown_argument_is_a_usage_error(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as raised:
        main(["--no-such-option"])

    assert raised.value.code == 2
    assert "unrecognized arguments" in capsys.readouterr().err


def test_option_abbreviations_are_rejected() -> None:
    # Abbreviations would turn every later option into a compatibility hazard.
    with pytest.raises(SystemExit) as raised:
        main(["--vers"])

    assert raised.value.code == 2
