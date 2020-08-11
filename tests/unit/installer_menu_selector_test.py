import subprocess
import sys

import pytest

from modules.installer_menu import Menu
from modules.menu_elements.exit import Exit

sys.path.append("./")  # noqa: E402


@pytest.fixture
def menu() -> Menu:
    return Menu()


@pytest.fixture
def menu_exit_element() -> Exit:
    return Exit()


def test_the_menu(menu):
    assert (
        "[red]>>>[/red] What do you need from the installer :question:" in menu.message
    )
    assert (
        "[bold red](C)[/bold red]heck the system requirements"
        in menu.steps[1]["stepDesc"]
    )
    assert "[bold red](T)[/bold red]est miniK8s" in menu.steps[2]["stepDesc"]
    assert "[bold red](I)[/bold red]nstall miniK8s" in menu.steps[3]["stepDesc"]
    assert "[bold red](E)[/bold red]xit" in menu.steps[4]["stepDesc"]


def test_the_action_class(menu_exit_element, capsys):
    menu_exit_element.perform_the_action(False)
    out, err = capsys.readouterr()
    assert out.startswith("Goodbye")
