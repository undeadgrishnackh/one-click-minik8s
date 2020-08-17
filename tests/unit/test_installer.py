import sys

import pytest

sys.path.append("./")  # noqa: E402
from modules.installer import Installer  # isort:skip  # noqa: E402
from tests.unit.doubles.fake_exit import FakeExit  # isort:skip # noqa: E402


@pytest.fixture(autouse=True)
def installer_console_output(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "e")
    monkeypatch.setattr("os._exit", lambda _: print("Exit request caught."))
    installer = Installer()
    installer.start()
    out, err = capsys.readouterr()
    return out


@pytest.fixture(autouse=True)
def installer_console_output_invalid_selection(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "exit")
    monkeypatch.setattr("os._exit", lambda _: print("Exit request caught."))
    installer = Installer()
    installer.start()
    out, err = capsys.readouterr()
    return out


@pytest.fixture(autouse=True)
def user_selection(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "e")
    monkeypatch.setattr("os._exit", lambda _: print("Exit request caught."))
    installer = Installer()
    installer.start()
    return installer.menu.user_selection


@pytest.fixture(autouse=True)
def installer_with_fake_exit_class_console_output(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "e")
    monkeypatch.setattr("os._exit", lambda _: print("Exit request caught."))
    installer = Installer()
    installer.start(fake_action_class=FakeExit())
    out, err = capsys.readouterr()
    return out


def test_expect_all_the_sub_modules_are_created():
    """🔬 expect all the sub modules are created"""
    installer = Installer()
    assert installer.console is not None
    assert installer.menu is not None
    assert installer.title is not None


def test_expect_the_title_is_displayed(installer_console_output):
    """🔬 expect the tile is displayed"""
    assert "Welcome to one-click-miniK8s" in installer_console_output


def test_expect_the_menu_is_displayed(installer_console_output):
    """🔬 expect the menu is displayed"""
    assert "What do you need from the installer" in installer_console_output


def test_expect_the_user_selects_an_invalid_option(
    installer_console_output_invalid_selection,
):
    """🔬 expect the user selects an invalid option"""
    assert "Invalid option!" in installer_console_output_invalid_selection


def test_expect_the_user_selects_a_valid_option(user_selection):
    """🔬 expect the user selects a valid option --> 'e'"""
    assert user_selection == "e"


def test_expect_the_installer_execs_the_related_option(
    installer_with_fake_exit_class_console_output,
):
    """🔬 expect the installer execs the related option"""
    assert (
        "Goodbye! From the Fake Exit ;)"
        in installer_with_fake_exit_class_console_output
    )
