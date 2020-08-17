import sys

import pytest

sys.path.append("./")  # noqa: E402
from modules.installer import Installer  # isort:skip  # noqa: E402
from tests.unit.doubles.fake_exit import FakeExit  # isort:skip # noqa: E402


def test_expect_all_the_sub_modules_are_created():
    """🔬 expect all the sub modules are created"""
    installer = Installer()
    assert installer.console is not None
    assert installer.menu is not None
    assert installer.title is not None


def test_expect_the_title_is_displayed(monkeypatch, capsys):
    """🔬 expect the tile is displayed"""
    monkeypatch.setattr("builtins.input", lambda _: "e")
    monkeypatch.setattr("os._exit", lambda _: print("Exit request caught."))
    installer = Installer()
    installer.start()
    out, err = capsys.readouterr()
    assert "Welcome to one-click-miniK8s" in out


def test_expect_the_menu_is_displayed(monkeypatch, capsys):
    """🔬 expect the menu is displayed"""
    monkeypatch.setattr("builtins.input", lambda _: "e")
    monkeypatch.setattr("os._exit", lambda _: print("Exit request caught."))
    installer = Installer()
    installer.start()
    out, err = capsys.readouterr()
    assert "What do you need from the installer" in out


def test_expect_the_user_selects_an_invalid_option(monkeypatch, capsys):
    """🔬 expect the user selects an invalid option"""
    monkeypatch.setattr("builtins.input", lambda _: "exit")
    monkeypatch.setattr("os._exit", lambda _: print("Exit request caught."))
    installer = Installer()
    installer.start()
    out, err = capsys.readouterr()
    assert "Invalid option!" in out


def test_expect_the_user_selects_a_valid_option(monkeypatch, capsys):
    """🔬 expect the user selects a valid option --> 'e'"""
    monkeypatch.setattr("builtins.input", lambda _: "e")
    monkeypatch.setattr("os._exit", lambda _: print("Exit request caught."))
    installer = Installer()
    installer.start()
    out, err = capsys.readouterr()
    assert installer.menu.user_selection == "e"


def test_expect_the_installer_execs_the_related_option(monkeypatch, capsys):
    """🔬 expect the installer execs the related option"""
    monkeypatch.setattr("builtins.input", lambda _: "e")
    monkeypatch.setattr("os._exit", lambda _: print("Exit request caught."))
    installer = Installer()
    installer.start(fake_action_class=FakeExit())
    out, err = capsys.readouterr()
    assert "Goodbye! From the Fake Exit ;)" in out
