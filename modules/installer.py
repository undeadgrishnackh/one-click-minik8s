from rich.console import Console

from modules.installer_menu import Menu
from modules.installer_title import Title


class Installer:
    def __init__(self):
        self.console = Console()
        self.menu = Menu()

    def start(self):
        Title().print_welcome_message()
        self.menu.print_the_menu_and_wait_the_answer()
        self.menu.perform_the_action()
