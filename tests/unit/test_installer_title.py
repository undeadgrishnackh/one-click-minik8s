import sys

import pytest
from rich.console import Console

sys.path.append("./")  # noqa: E402
from modules.installer_title import Title  # isort:skip  # noqa: E402


def test_is_rich_title():
    """🔬 expect the title is a rich text"""
    assert type(Title().console) is Console


def test_contains_the_tile(capsys):
    """🔬 expect a title message"""
    Title().print_welcome_message()
    out, err = capsys.readouterr()
    assert "Welcome to one-click-miniK8s" in out


def test_contains_the_separator(capsys):
    """🔬 expect a separator"""
    Title().print_welcome_message()
    out, err = capsys.readouterr()
    assert (
        "════════════════════════════════════════════════════════════════════════════════"
        in out
    )


def test_contains_the_descriptiopn(capsys):
    """🔬 expect a description message"""
    description = (
        "The idea behind this project is to provide a 'one-click' 🔘 installer 🏗️ as the \n"
        "welcome package for modern developers 👷 (Probably better to call them DevOps \n"
        "craftsmen/craftswomen)."
    )
    Title().print_welcome_message()
    out, err = capsys.readouterr()
    assert description in out
