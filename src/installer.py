from rich.console import Console

from src.console_markdown_welcome import Welcome
from src.installer_menu import Menu


class Installer:
    def __init__(self):
        self.console = Console()
        self.menu = Menu()

    def start(self):
        Welcome().print_welcome_message()
        self.menu.print_the_menu_and_wait_the_answer()
        self.menu.perform_the_action()
