from rich.console import Console
from rich.markdown import Markdown


class Welcome:
    def __init__(self):
        self.file = "doc/md/welcome.md"
        with open(self.file) as welcome:
            self.markdown = Markdown(welcome.read())

    def print_welcome_message(self):
        console = Console()
        console.print(self.markdown)
