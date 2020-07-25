import pytest
import sys 
from pytest_bdd import scenarios, given, when, then
sys.path.append('src/')
from welcome import Welcome


scenarios('../features/welcome_message.feature')


@pytest.fixture
def console_output():
    return Welcome().string


@given("I'm installing the dev env for K8s")
def installing_k8s():
    pass    


@when('the console print the welcome message')
@then('I read the render of the welcome.md file.')
def read_the_md_file(console_output):
    if "Welcome" in console_output:
        assert True
    else:
        assert False
    