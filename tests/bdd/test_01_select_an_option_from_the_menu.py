import subprocess
import sys

import pytest
from pytest_bdd import given, scenarios, then, when

sys.path.append("./")  # noqa: E402
from modules.installer import Installer  # isort:skip  # noqa: E402

scenarios("./features/test_select_an_option_from_the_menu.feature")


@pytest.fixture(scope="session", autouse=True)
def bash_installer_process_menu() -> subprocess.Popen:
    return subprocess.Popen(
        "./install_minik8s",
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )


@pytest.fixture(scope="session", autouse=True)
def bash_installer_process_that_take_the_test_action() -> subprocess.Popen:
    return subprocess.Popen(
        "./install_minik8s",
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )


@given("the user is installing the dev env for K8s")
def test_expect_k8s_installer_is_running(bash_installer_process_menu):
    assert type(bash_installer_process_menu) is subprocess.Popen


@given("is printed into the console a list of options")
def test_expect_the_menu_is_printed(bash_installer_process_menu):
    std_out = bash_installer_process_menu.communicate()[0]
    assert "What do you need from the installer" in std_out
    assert "(C)heck the system requirements" in std_out
    assert "(T)est miniK8s" in std_out
    assert "(I)nstall miniK8s" in std_out
    assert "(E)xit" in std_out


@when("the user selects the last one (EXIT)")
def simulate_the_user_selection_on_the_menu(
    bash_installer_process_that_take_the_test_action,
):
    bash_installer_process_that_take_the_test_action.communicate(input="e\n")


@then("the installer triggers the relative action")
@then("the installation exit with code 0.")
def test_expect_the_installer_quit_with_exit_code_zero(
    bash_installer_process_that_take_the_test_action,
):
    assert 0 == bash_installer_process_that_take_the_test_action.returncode
    bash_installer_process_that_take_the_test_action.kill()
