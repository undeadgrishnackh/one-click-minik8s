import sys

import pytest

sys.path.append("./")  # noqa: E402
from modules.installer import Installer  # isort:skip  # noqa: E402


def test_expect_all_the_sub_modules_are_created():
    """🔬 expect all the sub modules are created"""
    installer = Installer()
    assert installer.console is not None
    assert installer.menu is not None
    assert installer.title is not None


def test_expect_the_title_is_displayed(capsys):
    """🔬 expect the tile is displayed"""
    installer = Installer()
    installer.start(print_the_menu=False, wait_user_input=False)
    out, err = capsys.readouterr()
    assert "Welcome to one-click-miniK8s" in out


def test_expect_the_menu_is_displayed(capsys):
    """🔬 expect the menu is displayed"""
    installer = Installer()
    installer.start(wait_user_input=False)
    out, err = capsys.readouterr()
    assert "What do you need from the installer" in out


def test_expect_the_user_selects_an_invalid_option(capsys):
    """🔬 expect the user selects an invalid option"""
    installer = Installer()
    installer.start(wait_user_input=False, fake_user_selection="exit")
    out, err = capsys.readouterr()
    assert "Invalid option!" in out


def test_expect_the_user_selects_a_valid_option(capsys):
    """🔬 expect the user selects a valid option"""
    installer = Installer()
    installer.start(wait_user_input=False, fake_user_selection="e")
    out, err = capsys.readouterr()
    assert ">>> e" in out


def test_expect_the_installer_execs_the_related_option(capsys):
    """🔬 expect the installer execs the related option"""
    installer = Installer()
    installer.start(
        wait_user_input=False, fake_user_selection="e", fake_action_class=FakeExit()
    )
    out, err = capsys.readouterr()
    assert "Goodbye!" in out


class FakeExit:
    def __init__(self):
        self.exit_code = 0
        self.GOODBYE_MESSAGE = "Goodbye!"

    def perform_the_action(self):
        print(self.GOODBYE_MESSAGE)
