import subprocess
import sys

import pytest

sys.path.append("./")  # noqa: E402
from modules.installer_menu import Menu  # isort:skip # noqa: E402
from tests.unit.doubles.fake_exit import FakeExit  # isort:skip # noqa: E402


def test_the_menu_dictionary(menu):
    """🔬 expect the correct menu: question and options"""
    assert MENU_QUESTION == menu.menu_question
    assert MENU_ELEMENT_1 == menu.menu_options[1]["menu_option_desc"]
    assert MENU_ELEMENT_2 in menu.menu_options[2]["menu_option_desc"]
    assert MENU_ELEMENT_3 in menu.menu_options[3]["menu_option_desc"]
    assert MENU_ELEMENT_4 in menu.menu_options[4]["menu_option_desc"]


def test_the_menu_action_classes(menu):
    """🔬 expect the correct menu: classes to handle the user selection"""
    assert MENU_ACTION_CLASS_1 == menu.menu_options[1]["menu_option_action_class"]
    assert MENU_ACTION_CLASS_2 in menu.menu_options[2]["menu_option_action_class"]
    assert MENU_ACTION_CLASS_3 in menu.menu_options[3]["menu_option_action_class"]
    assert MENU_ACTION_CLASS_4 in menu.menu_options[4]["menu_option_action_class"]


def test_the_menu_option_shortcut(menu):
    """🔬 expect the correct menu: shortcut to activate an option"""
    assert MENU_SHORTCUT_1 == menu.menu_options[1]["menu_option_shortcut"]
    assert MENU_SHORTCUT_2 in menu.menu_options[2]["menu_option_shortcut"]
    assert MENU_SHORTCUT_3 in menu.menu_options[3]["menu_option_shortcut"]
    assert MENU_SHORTCUT_4 in menu.menu_options[4]["menu_option_shortcut"]


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


def test_stub_a_valid_user_input(valid_user_selection_key_stroke):
    """🔬 expect the menu gets the right user selection (builtins.input stubbed with an 'e')"""
    assert valid_user_selection_key_stroke == "e"


def test_stub_an_invalid_user_input(invalid_user_selection_stdout):
    """🔬 expect the menu gets the right user selection (builtins.input stubbed with an 'exit')"""
    assert "Invalid option!" in invalid_user_selection_stdout
    assert "Too many wrong selection! Program aborted." in invalid_user_selection_stdout


@pytest.mark.parametrize(
    "user_selection, expected_action_class",
    [("e", "Exit"), ("c", "Check"), ("t", "Test"), ("i", "Install")],
)
def test_stub_a_valid_option_to_check_the_related_action_class(
    menu_after_user_selection, user_selection, expected_action_class
):
    """❗ [ parametrize test] 🔬 expect the menu gets the right action - selection: e, c, t, i"""
    assert menu_after_user_selection.get_the_action_class() == expected_action_class


# TODO: this test has to be extended with the other menu actions.
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


# ######################################################################################################################
# CONSTANTS AND FIXTURES ###############################################################################################


MENU_QUESTION = "[red]>>>[/red] What do you need from the installer :question:"
MENU_ELEMENT_4 = "[bold red](E)[/bold red]xit"
MENU_ELEMENT_3 = "[bold red](I)[/bold red]nstall miniK8s"
MENU_ELEMENT_2 = "[bold red](T)[/bold red]est miniK8s"
MENU_ELEMENT_1 = "[bold red](C)[/bold red]heck the system requirements"

MENU_ACTION_CLASS_1 = "Check"
MENU_ACTION_CLASS_2 = "Test"
MENU_ACTION_CLASS_3 = "Install"
MENU_ACTION_CLASS_4 = "Exit"

MENU_SHORTCUT_1 = "C"
MENU_SHORTCUT_2 = "T"
MENU_SHORTCUT_3 = "I"
MENU_SHORTCUT_4 = "E"


@pytest.fixture(scope="module", autouse=True)
def menu() -> Menu:
    return Menu()


@pytest.fixture()
def valid_user_selection_key_stroke(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "e")
    return Menu().wait_the_answer()


@pytest.fixture()
def invalid_user_selection_stdout(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "exit")
    Menu().wait_the_answer()
    out, err = capsys.readouterr()
    return out


@pytest.fixture
def menu_after_user_selection(monkeypatch, user_selection):
    print(user_selection)
    monkeypatch.setattr("builtins.input", lambda _: user_selection)
    menu = Menu()
    menu.wait_the_answer()
    return menu
