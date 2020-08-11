from rich.console import Console


class Title:
    def __init__(self):
        self.console = Console()

    def print_welcome_message(self):
        self.console.print("[red bold]Welcome to one-click-miniK8s![/red bold]")
        self.console.print(
            "[red]════════════════════════════════════════════════════════════════════════════════["
            "/red]"
        )
        self.console.print(
            "The idea behind this project is to provide a 'one-click' installer as the \n"
            "welcome package for modern developers (Probably better to call them DevOps \n"
            "craftsmen/craftswomen)."
        )
