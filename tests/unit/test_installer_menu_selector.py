import subprocess
import sys

import pytest

sys.path.append("./")  # noqa: E402
from modules.installer_menu import Menu  # isort:skip # noqa: E402
from tests.unit.doubles.fake_exit import FakeExit  # isort:skip # noqa: E402


@pytest.fixture(scope="module", autouse=True)
def menu() -> Menu:
    return Menu()


def test_the_menu_dictionary(menu):
    """🔬 expect the correct menu: question and options"""
    question = "[red]>>>[/red] What do you need from the installer :question:"
    menu_element_1 = "[bold red](C)[/bold red]heck the system requirements"
    menu_element_2 = "[bold red](T)[/bold red]est miniK8s"
    menu_element_3 = "[bold red](I)[/bold red]nstall miniK8s"
    menu_element_4 = "[bold red](E)[/bold red]xit"
    assert question == menu.menu_question
    assert menu_element_1 == menu.menu_options[1]["menu_option_desc"]
    assert menu_element_2 in menu.menu_options[2]["menu_option_desc"]
    assert menu_element_3 in menu.menu_options[3]["menu_option_desc"]
    assert menu_element_4 in menu.menu_options[4]["menu_option_desc"]


def test_the_menu_action_classes(menu):
    """🔬 expect the correct menu: classes to handle the user selection"""
    menu_action_class_1 = "Check"
    menu_action_class_2 = "Test"
    menu_action_class_3 = "Install"
    menu_action_class_4 = "Exit"
    assert menu_action_class_1 == menu.menu_options[1]["menu_option_action_class"]
    assert menu_action_class_2 in menu.menu_options[2]["menu_option_action_class"]
    assert menu_action_class_3 in menu.menu_options[3]["menu_option_action_class"]
    assert menu_action_class_4 in menu.menu_options[4]["menu_option_action_class"]


def test_the_menu_option_shortcut(menu):
    """🔬 expect the correct menu: shortcut to activate an option"""
    menu_shortcut_1 = "C"
    menu_shortcut_2 = "T"
    menu_shortcut_3 = "I"
    menu_shortcut_4 = "E"
    assert menu_shortcut_1 == menu.menu_options[1]["menu_option_shortcut"]
    assert menu_shortcut_2 in menu.menu_options[2]["menu_option_shortcut"]
    assert menu_shortcut_3 in menu.menu_options[3]["menu_option_shortcut"]
    assert menu_shortcut_4 in menu.menu_options[4]["menu_option_shortcut"]


def test_how_is_printed_the_menu(capsys):
    """🔬 expect the menu is printed correctly on the terminal (strict test)"""
    Menu().print_the_menu()
    out, err = capsys.readouterr()
    assert "┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓" in out
    assert "┃ >>> What do you need from the installer ❓ ┃" in out
    assert "┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩" in out
    assert "│ (C)heck the system requirements            │" in out
    assert "│ (T)est miniK8s                             │" in out
    assert "│ (I)nstall miniK8s                          │" in out
    assert "│ (E)xit                                     │" in out
    assert "└────────────────────────────────────────────┘" in out


def test_stub_a_valid_user_input(monkeypatch):
    """🔬 expect the menu gets the right user selection (builtins.input stubbed with an 'e')"""
    monkeypatch.setattr("builtins.input", lambda _: "e")
    user_selection = Menu().wait_the_answer()
    assert user_selection == "e"


def test_stub_an_invalid_user_input(monkeypatch, capsys):
    """🔬 expect the menu gets the right user selection (builtins.input stubbed with an 'exit')"""
    monkeypatch.setattr("builtins.input", lambda _: "exit")
    Menu().wait_the_answer()
    out, err = capsys.readouterr()
    assert "Invalid option!" in out
    assert "Too many wrong selection! Program aborted." in out


def test_the_action_class_exit(monkeypatch):
    """🔬 expect the menu gets the right action class after the user selected 'e' (Exit)"""
    monkeypatch.setattr("builtins.input", lambda _: "e")
    menu = Menu()
    menu.wait_the_answer()
    assert menu.get_the_action_class() == "Exit"


def test_the_action_class_check(monkeypatch):
    """🔬 expect the menu gets the right action class after the user selected 'c' (Check)"""
    monkeypatch.setattr("builtins.input", lambda _: "c")
    menu = Menu()
    menu.wait_the_answer()
    assert menu.get_the_action_class() == "Check"


def test_the_action_class_test(monkeypatch):
    """🔬 expect the menu gets the right action class after the user selected 't' (Test)"""
    monkeypatch.setattr("builtins.input", lambda _: "t")
    menu = Menu()
    menu.wait_the_answer()
    assert menu.get_the_action_class() == "Test"


def test_the_action_class_install(monkeypatch):
    """🔬 expect the menu gets the right action class after the user selected 'i' (Install)"""
    monkeypatch.setattr("builtins.input", lambda _: "i")
    menu = Menu()
    menu.wait_the_answer()
    assert menu.get_the_action_class() == "Install"


def test_perform_the_action_exit(monkeypatch, capsys):
    """🔬 expect to spy an os.exit after selecting 'e' (Exit)"""
    monkeypatch.setattr("builtins.input", lambda _: "e")
    monkeypatch.setattr("os._exit", lambda _: print("Exit request caught."))
    menu = Menu()
    menu.wait_the_answer()
    menu.perform_the_action()
    out, err = capsys.readouterr()
    assert "Exit request caught." in out
    assert "Goodbye!" in out
