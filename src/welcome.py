from rich.console import Console
from rich.markdown import Markdown


class Welcome:
    def __init__(self):
        self.file = "doc/md/welcome.md"
        with open(self.file) as welcome:
            markdown = Markdown(welcome.read())
            self.markdown = markdown
            self.string = markdown.markup


console = Console()
console.print(Welcome().markdown)
