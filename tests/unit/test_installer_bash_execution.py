import subprocess
import sys

import pytest

sys.path.append("./")  # noqa: E402
from modules.installer import Installer  # isort:skip # noqa: E402


@pytest.fixture(autouse=True)
def install_process():
    return subprocess.Popen("./install_minik8s", stdout=subprocess.PIPE)


@pytest.fixture(autouse=True)
def install_process_pid(install_process):
    return install_process.pid


def test_exec_the_installer_and_get_the_pid(install_process_pid):
    """🔬 expect a valid PID executing the install_minik8s"""
    assert install_process_pid is not None


def pytest_sessionfinish(session, exitstatus):
    install_process.terminate()
