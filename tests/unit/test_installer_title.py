import sys

import pytest
from rich.console import Console

sys.path.append("./")  # noqa: E402
from modules.installer_title import Title  # isort:skip  # noqa: E402


@pytest.fixture()
def title_stdout(capsys):
    Title().print_welcome_message()
    out, err = capsys.readouterr()
    return out


def test_is_rich_title():
    """🔬 expect the title is a rich text"""
    assert type(Title().console) is Console


def test_contains_the_tile(title_stdout):
    """🔬 expect a title message"""
    title_welcome = "Welcome to one-click-miniK8s"
    assert title_welcome in title_stdout


def test_contains_the_separator(title_stdout):
    """🔬 expect a separator"""
    title_separator = "════════════════════════════════════════════════════════════════════════════════"
    assert title_separator in title_stdout


def test_contains_the_description(title_stdout):
    """🔬 expect a description message"""
    description = (
        "The idea behind this project is to provide a 'one-click' 🔘 installer 🏗️ as the \n"
        "welcome package for modern developers 👷 (Probably better to call them DevOps \n"
        "craftsmen/craftswomen)."
    )
    assert description in title_stdout
