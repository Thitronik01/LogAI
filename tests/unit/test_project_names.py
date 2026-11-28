"""The project name is provisional: it must be spelled out in exactly one place."""

import tomllib
from pathlib import Path

from logai_scan import names

REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = REPO_ROOT / "src"
TEXT_SUFFIXES = frozenset(
    {".css", ".html", ".j2", ".json", ".md", ".py", ".toml", ".txt", ".yaml", ".yml"}
)


def test_the_name_is_spelled_out_in_one_module_only() -> None:
    names_module = Path(names.__file__).resolve()
    # The import package name is unavoidable in import statements and does not count.
    import_name = names.__name__.partition(".")[0]
    needle = names.PROJECT_NAME.casefold()

    offenders: list[str] = []
    for path in sorted(SOURCE_ROOT.rglob("*")):
        if path.suffix not in TEXT_SUFFIXES or path.resolve() == names_module:
            continue
        text = path.read_text(encoding="utf-8").replace(import_name, "")
        if needle in text.casefold():
            offenders.append(path.relative_to(REPO_ROOT).as_posix())

    assert offenders == [], f"import the name from {names.__name__} instead"


def test_packaging_metadata_matches_the_constants() -> None:
    pyproject = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    project = pyproject["project"]

    assert project["name"] == names.DISTRIBUTION_NAME
    assert list(project["scripts"]) == [names.COMMAND_NAME]


def test_the_command_points_at_the_import_package() -> None:
    pyproject = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    target: str = pyproject["project"]["scripts"][names.COMMAND_NAME]

    assert target.partition(".")[0] == names.__name__.partition(".")[0]
