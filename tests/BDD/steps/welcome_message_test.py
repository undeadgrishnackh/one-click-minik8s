from pytest_bdd import scenarios, given, when, then

scenarios('../features/welcome_message.feature')


@given("I'm installing the dev env for K8s")
def installing_k8s():
    pass


@when('the console print the welcome message')
@then('I read the render of the welcome.md file.')
def read_the_md_file():
    assert True
