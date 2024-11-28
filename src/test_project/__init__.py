"""
Package description.
"""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("test-project")
except PackageNotFoundError:
    __version__ = "uninstalled"