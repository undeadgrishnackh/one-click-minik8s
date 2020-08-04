from rich.console import Console

from src.console_markdown_welcome import Welcome


class Installer:
    def __init__(self):
        self.console = Console()

    def start(self):
        Welcome().print_welcome_message()
