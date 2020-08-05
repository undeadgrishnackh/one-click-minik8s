import subprocess
import sys

import pytest
from pytest_bdd import given, scenarios, then, when

from src.bash_installer import Installer

scenarios("./features/select_an_option.feature")


@pytest.fixture
def bash_installer_process():
    return subprocess.Popen("./install_minik8s", stdout=subprocess.PIPE)


@pytest.fixture
def bash_installer_output(bash_installer_process):
    return bash_installer_process.communicate()[0]


@given("the user is installing the dev env for K8s")
def exec_k8s_installer(bash_installer_process):
    assert type(bash_installer_process) is subprocess.Popen


@given("is printed into the console a list of options")
def check_the_options():
    assert False is True


@when("the user selects one of them")
def sniff_the_user_selection():
    assert False is True


@then("the installer triggers the relative action.")
def take_action():
    assert False is True
