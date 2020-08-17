import subprocess
import sys

import pytest
from pytest_bdd import given, scenarios, then, when

sys.path.append("./")  # noqa: E402
from modules.installer import Installer  # isort:skip  # noqa: E402

scenarios("./features/01_select_an_option_from_the_menu.feature")


@pytest.fixture(scope="session", autouse=True)
def bash_installer_process() -> subprocess.Popen:
    return subprocess.Popen(
        "./install_minik8s",
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )


@pytest.fixture(scope="session", autouse=True)
def bash_installer_process_after_the_action(bash_installer_process):
    stdout, stderr = bash_installer_process.communicate(input="e\n", timeout=2)
    return stdout


@given("the user is installing the dev env for K8s")
def test_expect_k8s_installer_is_running(bash_installer_process):
    assert type(bash_installer_process) is subprocess.Popen


@given("is printed into the console the menu's options")
def test_expect_the_menu_is_printed(bash_installer_process_after_the_action):
    """🧬 expect the menu is visualized"""
    assert (
        "What do you need from the installer" in bash_installer_process_after_the_action
    )
    assert "(C)heck the system requirements" in bash_installer_process_after_the_action
    assert "(T)est miniK8s" in bash_installer_process_after_the_action
    assert "(I)nstall miniK8s" in bash_installer_process_after_the_action
    assert "(E)xit" in bash_installer_process_after_the_action


@when("the user selects the last one (EXIT)")
def test_expect_the_user_selection_on_the_menu(bash_installer_process_after_the_action):
    """🧬 expect the user selected the option 'Exit'"""
    assert ">>> " in bash_installer_process_after_the_action


@then("the installer triggers the relative action")
@then("the installation quit with exit code 0.")
def test_expect_the_installer_quit_with_exit_code_zero(bash_installer_process):
    """🧬 expect the installer ended with exit code zero."""
    assert 0 == bash_installer_process.returncode
    bash_installer_process.terminate()
