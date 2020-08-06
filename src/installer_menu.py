import inquirer
from menu_options.exit import Exit
from rich.console import Console


class Menu:
    def __init__(self):
        self.console = Console()

    steps = {
        1: {"stepDesc": "Check the system requirements", "optionClass": "Check"},
        2: {"stepDesc": "Test miniK8s", "optionClass": "Test"},
        3: {"stepDesc": "Install miniK8s", "optionClass": "Install"},
        4: {"stepDesc": "Exit", "optionClass": "Exit"},
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
                return self.steps[index]["optionClass"]
            pass
        return None


# TODO: create a metod to handle the menu interaction - The spike to delegate the class creation at run time is working.
installer = Menu()
installer.get_the_answer()
optionClass = installer.get_the_action()
globals()[optionClass]().perform_the_action()
