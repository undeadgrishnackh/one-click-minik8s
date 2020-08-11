from rich.console import Console

from modules.console_markdown_welcome import Welcome
from modules.installer_menu import Menu


class Installer:
    def __init__(self):
        self.console = Console()
        self.menu = Menu()

    def start(self):
        Welcome().print_welcome_message()
        self.menu.print_the_menu_and_wait_the_answer()
        self.menu.perform_the_action()
