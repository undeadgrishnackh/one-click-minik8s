import subprocess
import sys

import pytest

from src.bash_installer import Installer


def test_exec_the_installer_and_get_the_welcome_message():
    cmdProcess = subprocess.Popen("./install_minik8s", stdout=subprocess.PIPE)
    cmdOut = cmdProcess.communicate()[0]
    # the console flush a bytestream, so the assert has to be as byte: b"pattern"
    assert b"Welcome to one-click-miniK8s" in cmdOut
