import subprocess
import sys

import pytest

sys.path.append("./")  # noqa: E402
from modules.installer import Installer  # isort:skip # noqa: E402


def test_exec_the_installer_and_get_the_pid():
    """🔬 expect a valid PID executing the install_minik8s"""
    cmd_process = subprocess.Popen("./install_minik8s", stdout=subprocess.PIPE)
    assert cmd_process.pid is not None
    cmd_process.terminate()
