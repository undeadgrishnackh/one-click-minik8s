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

    def start(self, print_the_menu=True, ask_the_user=True, fake_user_selection=None):
        self.title.print_welcome_message()
        if print_the_menu:
            self.menu.print_the_menu_and_wait_the_answer(
                ask_the_user, fake_user_selection
            )
            if ask_the_user:
                self.menu.perform_the_action()
