import subprocess
import sys

import pytest
from pytest_bdd import given, scenarios, then, when

from src.installer import Installer

scenarios("./features/welcome_message.feature")


@pytest.fixture(scope="session", autouse=True)
def bash_installer_process():
    return subprocess.Popen("./install_minik8s", stdout=subprocess.PIPE)


@pytest.fixture(scope="session", autouse=True)
def bash_installer_output(bash_installer_process):
    return bash_installer_process.communicate()[0]


@given("I'm installing the dev env for K8s")
def exec_k8s_installer(bash_installer_process):
    assert type(bash_installer_process) is subprocess.Popen


@when("the console print the welcome message")
def sniff_the_output_buffer(bash_installer_output):
    assert bash_installer_output != ""


@then("I read the render of the welcome.md file.")
def read_the_md_file(bash_installer_output, bash_installer_process):
    assert b"Welcome" in bash_installer_output
    bash_installer_process.kill()
