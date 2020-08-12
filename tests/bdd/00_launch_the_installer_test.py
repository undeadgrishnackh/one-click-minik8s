import subprocess
import sys

import pytest
from pytest_bdd import given, scenarios, then, when

sys.path.append("./")  # noqa: E402
from modules.installer import Installer  # isort:skip # noqa: E402

scenarios("./features/welcome_message.feature")


@pytest.fixture(scope="session", autouse=True)
def bash_installer_process():
    return subprocess.Popen("./install_minik8s", stdout=subprocess.PIPE)


@pytest.fixture(scope="session", autouse=True)
def bash_installer_output(bash_installer_process):
    return bash_installer_process.communicate()[0]


@given("I'm installing the dev env for K8s")
def test_expect_the_k8s_installer_is_running(bash_installer_process):
    assert type(bash_installer_process) is subprocess.Popen


@when("the console print the title")
def test_expect_the_installer_is_printing_something(bash_installer_output):
    assert bash_installer_output != ""


@then("I read it as rich text.")
def test_expect_the_tile_is_printed(bash_installer_output, bash_installer_process):
    assert b"Welcome to one-click-miniK8s!\n" in bash_installer_output
    bash_installer_process.kill()
