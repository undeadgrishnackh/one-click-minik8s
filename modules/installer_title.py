from rich.console import Console

WELCOME_MESSAGE = "[red bold]Welcome to one-click-miniK8s![/red bold]"
SEPARATOR = "[red]════════════════════════════════════════════════════════════════════════════════[/red]"
DESCRIPTION = (
    "The idea behind this project is to provide a 'one-click' 🔘 installer 🏗️ as the \n"
    "welcome package for modern developers 👷 (Probably better to call them DevOps \n"
    "craftsmen/craftswomen)."
)


class Title:
    def __init__(self):
        self.console = Console()
        self.title = WELCOME_MESSAGE
        self.separator = SEPARATOR
        self.description = DESCRIPTION

    def print_welcome_message(self):
        self.console.print("%s" % WELCOME_MESSAGE)
        self.console.print("%s" % SEPARATOR)
        self.console.print("%s" % DESCRIPTION)
