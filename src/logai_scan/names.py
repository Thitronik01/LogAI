"""The project's names, defined once.

The project name is provisional and may still change. Nothing else in the source tree
spells it out: code that needs a name imports it from here. The only unavoidable copies
are the import package name (the directory this file lives in) and ``pyproject.toml``;
``tests/unit/test_project_names.py`` keeps all of them consistent.
"""

from typing import Final

PROJECT_NAME: Final = "LogAI"
"""Name used in prose, for example in help texts and report headings."""

DISTRIBUTION_NAME: Final = "logai-scan"
"""Name of the installable distribution."""

COMMAND_NAME: Final = "logai"
"""Name of the command-line program."""
