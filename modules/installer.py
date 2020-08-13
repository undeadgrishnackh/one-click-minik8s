import sys

from rich.console import Console

sys.path.append("./")  # noqa: E402
from modules.installer_menu import Menu  # isort:skip  # noqa: E402
from modules.installer_title import Title  # isort:skip  # noqa: E402


class Installer:
    def __init__(self):
        self.console = Console()
        self.menu = Menu()
        self.title = Title()

    def start(
        self,
        print_the_menu=True,
        wait_user_input=True,
        fake_user_selection=None,
        fake_action_class=None,
    ):
        self.title.print_welcome_message()
        self.menu.print_the_menu(print_the_menu)
        if wait_user_input:
            self.menu.wait_the_answer()
            self.menu.perform_the_action()
        else:
            self.menu.wait_the_answer(wait_user_input, fake_user_selection)
            if fake_action_class is not None:
                self.menu.perform_the_action(fake_action_class)
