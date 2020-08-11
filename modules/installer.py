import sys

from rich.console import Console

sys.path.append("./")  # noqa: E402
from modules.installer_menu import Menu  # isort:skip  # noqa: E402
from modules.installer_title import Title  # isort:skip  # noqa: E402


class Installer:
    def __init__(self):
        self.console = Console()
        self.menu = Menu()

    def start(self):
        Title().print_welcome_message()
        self.menu.print_the_menu_and_wait_the_answer()
        self.menu.perform_the_action()
