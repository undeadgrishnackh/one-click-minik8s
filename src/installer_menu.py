from rich.console import Console
from rich.table import Table

from src.menu_elements.exit import Exit


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

    def print_the_menu_and_wait_the_answer(self):
        table = Table()
        table.add_column(self.message, justify="left", style="white", no_wrap=True)
        for index in self.steps:
            table.add_row(self.steps[index]["stepDesc"])
            pass
        self.console.print(table)
        self.get_a_valid_answer()

    def get_a_valid_answer(self):
        self.answer = input(">>> ")
        for index in self.steps:
            if self.answer.upper() == self.steps[index]["stepKey"].upper():
                return
            pass
        self.console.print("[bold red]Invalid option![/bold red]")
        self.get_a_valid_answer()

    def get_the_action_class(self):
        for index in self.steps:
            if self.answer.upper() == self.steps[index]["stepKey"].upper():
                return self.steps[index]["optionClass"]
            pass
        return None

    def perform_the_action(self):
        menu_element_implementation = self.get_the_action_class()
        globals()[menu_element_implementation]().perform_the_action()
