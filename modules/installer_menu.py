from rich.console import Console
from rich.table import Table

from modules.menu_elements.exit import Exit


class Menu:
    def __init__(self):
        self.console = Console()

    steps = {
        1: {
            "stepDesc": "[bold red](C)[/bold red]heck the system requirements",
            "stepKey": "C",
            "optionClass": "Check",
        },
        2: {
            "stepDesc": "[bold red](T)[/bold red]est miniK8s",
            "stepKey": "T",
            "optionClass": "Test",
        },
        3: {
            "stepDesc": "[bold red](I)[/bold red]nstall miniK8s",
            "stepKey": "I",
            "optionClass": "Install",
        },
        4: {
            "stepDesc": "[bold red](E)[/bold red]xit",
            "stepKey": "E",
            "optionClass": "Exit",
        },
    }
    message = "[red]>>>[/red] What do you need from the installer :question:"
    answer = ""

    def print_the_menu(self, print_the_menu=True):
        if print_the_menu:
            table = Table()
            table.add_column(self.message, justify="left", style="white", no_wrap=True)
            for index in self.steps:
                table.add_row(self.steps[index]["stepDesc"])
                pass
            self.console.print(table)

    def wait_the_answer(self, wait_user_input=True, fake_user_selection=None):
        if wait_user_input:
            self.get_a_valid_answer()
        if fake_user_selection:
            self.get_a_valid_answer(fake_user_selection)

    def get_a_valid_answer(self, fake_user_selection=None):
        if fake_user_selection is None:
            self.answer = input(">>> ")
            self.check_if_is_a_valid_answer()
        else:
            self.console.print(">>> " + fake_user_selection)
            self.answer = fake_user_selection
            self.check_if_is_a_valid_answer(fake_user_selection)

    def check_if_is_a_valid_answer(self, fake_user_selection=None):
        for index in self.steps:
            if self.answer.upper() == self.steps[index]["stepKey"].upper():
                return
            pass
        self.console.print("[bold red]Invalid option![/bold red]")
        if fake_user_selection is None:
            self.get_a_valid_answer()

    def get_the_action_class(self):
        for index in self.steps:
            if self.answer.upper() == self.steps[index]["stepKey"].upper():
                return self.steps[index]["optionClass"]
            pass
        return None

    def perform_the_action(self, fake_action_class=None):
        if fake_action_class is None:
            menu_element_implementation = self.get_the_action_class()
            globals()[menu_element_implementation]().perform_the_action()
        else:
            menu_element_implementation = fake_action_class
            fake_action_class.perform_the_action()
