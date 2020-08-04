import pytest
import sys
from pytest_bdd import scenarios, given, when, then
from src.welcome import Welcome


scenarios('../features/welcome_message.feature')


@pytest.fixture
def console_output():
    return Welcome().markdown.markup


@given("I'm installing the dev env for K8s")
def exec_k8s_installer():
    # must handle and trap the bash process
    assert True


@when('the console print the welcome message')
def sniff_the_output_buffer():
    # the output buffer must be not empty
    assert True    


@then('I read the render of the welcome.md file.')
def read_the_md_file(console_output):
    assert "Welcome" in console_output
