import sys

import pytest

sys.path.append("./")  # noqa: E402
from modules.installer import Installer  # isort:skip  # noqa: E402


def test_expect_all_the_sub_modules_are_created():
    installer = Installer()
    assert installer.console is not None
    assert installer.menu is not None
    assert installer.title is not None


def test_expect_the_title_is_displayed(capsys):
    installer = Installer()
    installer.start(print_the_menu=False)
    out, err = capsys.readouterr()
    assert "Welcome to one-click-miniK8s" in out


def test_expect_the_menu_is_displayed(capsys):
    installer = Installer()
    installer.start(ask_the_user=False)
    out, err = capsys.readouterr()
    assert "What do you need from the installer" in out
