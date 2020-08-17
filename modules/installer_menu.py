from rich.console import Console
from rich.table import Table

from modules.menu_elements.exit import Exit


class Menu:
    def __init__(self):
        self.console = Console()
        self.wrong_selection = 0

    menu_options = {
        1: {
            "menu_option_desc": "[bold red](C)[/bold red]heck the system requirements",
            "menu_option_shortcut": "C",
            "menu_option_action_class": "Check",
        },
        2: {
            "menu_option_desc": "[bold red](T)[/bold red]est miniK8s",
            "menu_option_shortcut": "T",
            "menu_option_action_class": "Test",
        },
        3: {
            "menu_option_desc": "[bold red](I)[/bold red]nstall miniK8s",
            "menu_option_shortcut": "I",
            "menu_option_action_class": "Install",
        },
        4: {
            "menu_option_desc": "[bold red](E)[/bold red]xit",
            "menu_option_shortcut": "E",
            "menu_option_action_class": "Exit",
        },
    }
    menu_question = "[red]>>>[/red] What do you need from the installer :question:"
    user_selection = ""

    def print_the_menu(self):
        table = Table()
        table.add_column(
            self.menu_question, justify="left", style="white", no_wrap=True
        )
        for index in self.menu_options:
            table.add_row(self.menu_options[index]["menu_option_desc"])
        self.console.print(table)

    def wait_the_answer(self):
        self.get_a_valid_answer()
        return self.user_selection

    def get_a_valid_answer(self):
        self.user_selection = input(">>> ")
        self.check_if_is_a_valid_answer()

    def check_if_is_a_valid_answer(self):
        for index in self.menu_options:
            if (
                self.user_selection.upper()
                == self.menu_options[index]["menu_option_shortcut"].upper()
            ):
                self.wrong_selection = 0
                return
        self.console.print("[bold red]Invalid option![/bold red]")
        if self.wrong_selection >= 3:
            print("Too many wrong selection! Program aborted.")
            self.user_selection = "e"
            return
        else:
            self.wrong_selection += 1
        self.get_a_valid_answer()

    def get_the_action_class(self):
        for index in self.menu_options:
            if (
                self.user_selection.upper()
                == self.menu_options[index]["menu_option_shortcut"].upper()
            ):
                return self.menu_options[index]["menu_option_action_class"]

    def perform_the_action(self, fake_action_class=None):
        if fake_action_class is None:
            menu_element_implementation = self.get_the_action_class()
            globals()[menu_element_implementation]().perform_the_action()
        else:
            menu_element_implementation = fake_action_class
            fake_action_class.perform_the_action()
