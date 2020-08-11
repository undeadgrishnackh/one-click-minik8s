import subprocess
import sys

import pytest
from pytest_bdd import given, scenarios, then, when

sys.path.append("./")  # noqa: E402
from modules.installer import Installer  # isort:skip  # noqa: E402

scenarios("./features/select_an_option_from_the_menu_test.feature")


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
def bash_installer_process_action() -> subprocess.Popen:
    return subprocess.Popen(
        "./install_minik8s",
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )


@given("the user is installing the dev env for K8s")
def exec_k8s_installer(bash_installer_process_menu):
    assert type(bash_installer_process_menu) is subprocess.Popen


@given("is printed into the console a list of options")
def check_the_options(bash_installer_process_menu):
    std_out = bash_installer_process_menu.communicate()[0]
    assert "What do you need from the installer" in std_out
    assert "(C)heck the system requirements" in std_out
    assert "(T)est miniK8s" in std_out
    assert "(I)nstall miniK8s" in std_out
    assert "(E)xit" in std_out


@when("the user selects the last one (EXIT)")
def sniff_the_user_selection(bash_installer_process_action):
    bash_installer_process_action.communicate(input="e\n")


@then("the installer triggers the relative action")
@then("the installation exit with code 0.")
def take_action(bash_installer_process_action):
    assert 0 == bash_installer_process_action.returncode
    bash_installer_process_action.kill()
