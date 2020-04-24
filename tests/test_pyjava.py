import logging

from pyjava import get_jre_path

_LOGGER = logging.getLogger(__name__)

def test_get_java():
    pth = get_jre_path()

    assert pth.exists()
    assert pth.name == "java.exe"
