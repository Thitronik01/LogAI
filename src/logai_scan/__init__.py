"""Offline analysis of log exports that shows which AI services were reached from a network."""

from importlib.metadata import PackageNotFoundError, version

from logai_scan.names import DISTRIBUTION_NAME

try:
    __version__ = version(DISTRIBUTION_NAME)
except PackageNotFoundError:  # pragma: no cover - only when run from an uninstalled source tree
    __version__ = "0+unknown"

__all__ = ["__version__"]
