import inquirer
from rich.console import Console


class Step:
    def __init__(self):
        self.console = Console()

    steps = {
        1: {"stepDesc": "Check the system requirements", "stepAction": "check"},
        2: {"stepDesc": "Test miniK8s", "stepAction": "test"},
        3: {"stepDesc": "Install miniK8s", "stepAction": "install"},
        4: {"stepDesc": "Exit", "stepAction": "exit"},
    }
    choices = []
    message = "What do you need from the installer?"
    answer = ""

    def get_options(self):
        for index in self.steps:
            self.choices.append(self.steps[index]["stepDesc"])
            pass
        return self.choices

    def get_the_answer(self):
        self.answer = inquirer.prompt(
            [inquirer.List("step", message=self.message, choices=self.get_options())]
        )
        print(self.answer)

    def get_the_action(self):
        for index in self.steps:
            if self.answer["step"] == self.steps[index]["stepDesc"]:
                return self.steps[index]["stepAction"]
            pass
        return None


installer = Step()
installer.get_the_answer()
print(installer.get_the_action())


# TODO: the spike with the selector is done. Now revert and create the tests for the selection.
