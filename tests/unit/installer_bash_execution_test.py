import subprocess
import sys

import pytest

sys.path.append("./")  # noqa: E402
from modules.installer import Installer  # isort:skip # noqa: E402


def test_exec_the_installer_and_get_the_welcome_message():
    cmd_process = subprocess.Popen("./install_minik8s", stdout=subprocess.PIPE)
    cmd_out = cmd_process.communicate()[0]
    # the console flush a bytestream, so the assert has to be as byte: b"pattern"
    assert b"Welcome to one-click-miniK8s" in cmd_out
