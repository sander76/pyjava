"""Java runtime to be used inside python."""

import logging
from pathlib import Path

_LOGGER = logging.getLogger(__name__)

__version__ = "0.0.1"

HERE = Path(__file__).parent


def get_jre_path() -> Path:
    """Return the location of the java runtime."""
    return HERE / "jre8" / "bin" / "java.exe"
