"""The catalog check must not report success for a validation that did not happen."""

from pathlib import Path

import pytest
import validate_catalog


def test_without_a_catalog_it_says_that_nothing_was_validated(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    assert validate_catalog.main([str(tmp_path / "catalog")]) == 0
    assert "nothing was validated" in capsys.readouterr().out


def test_it_fails_once_catalog_content_exists(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    catalog_dir = tmp_path / "catalog"
    catalog_dir.mkdir()

    assert validate_catalog.main([str(catalog_dir)]) == 1
    assert "not implemented yet" in capsys.readouterr().err


def test_the_notice_is_surfaced_in_github_actions(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("GITHUB_ACTIONS", "true")

    validate_catalog.main([str(tmp_path / "catalog")])

    assert "::notice title=Catalog validation::" in capsys.readouterr().out
