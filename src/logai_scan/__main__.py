"""Allow ``python -m`` invocation of the command-line program."""

import sys

from logai_scan.cli import main

if __name__ == "__main__":
    sys.exit(main())
