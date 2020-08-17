import subprocess
import sys

import pytest
from pytest_bdd import given, scenarios, then, when

sys.path.append("./")  # noqa: E402
from modules.installer import Installer  # isort:skip # noqa: E402

scenarios("./features/00_launch_the_installer.feature")


i_am_still_alive = None


@pytest.fixture(scope="session", autouse=True)
def bash_installer_process() -> subprocess.Popen:
    return subprocess.Popen("./install_minik8s", stdout=subprocess.PIPE, shell=False)


@pytest.fixture(scope="session", autouse=True)
def bash_installer_output(bash_installer_process):
    stdout, stderr = bash_installer_process.communicate()
    return stdout


@given("I'm installing the dev env for K8s")
def test_expect_the_k8s_installer_is_running(bash_installer_process):
    assert type(bash_installer_process) is subprocess.Popen


@when("the console print the title")
def test_expect_the_installer_is_printing_the_title(bash_installer_output):
    """🧬 expect the console contains the installer's title"""
    assert b"Welcome to one-click-miniK8s!" in bash_installer_output


@then("the installer quits.")
def test_expect_the_installer_quits(bash_installer_process):
    """🧬 expect the installer quits"""
    bash_installer_process.terminate()
    assert bash_installer_process.returncode is not i_am_still_alive
