"""Validate the service catalog.

The catalog schema and the first entries arrive with the first-scan milestone. Until
then there is nothing to validate, and this script says so instead of reporting success
for a check that did not happen. It fails as soon as a catalog directory exists, so that
catalog content cannot be merged before the real validation is in place.
"""

import argparse
import os
import sys
from collections.abc import Sequence
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def _notice(message: str) -> None:
    print(message)
    if os.environ.get("GITHUB_ACTIONS") == "true":
        # Surfaces the message on the summary page of the workflow run.
        print(f"::notice title=Catalog validation::{message}")


def main(argv: Sequence[str] | None = None) -> int:
    """Validate the catalog and return the exit status."""
    parser = argparse.ArgumentParser(description="Validate the service catalog.")
    parser.add_argument(
        "catalog_dir",
        nargs="?",
        type=Path,
        default=REPO_ROOT / "catalog",
        help="directory that holds the catalog (default: %(default)s)",
    )
    catalog_dir: Path = parser.parse_args(argv).catalog_dir

    if not catalog_dir.exists():
        _notice("No catalog directory yet: nothing was validated.")
        return 0

    print(
        f"error: {catalog_dir} exists, but catalog validation is not implemented yet. "
        "Catalog content must not be added before its validation.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
