import sys

import pytest
from rich.markdown import Markdown

sys.path.append("./")  # noqa: E402
from modules.installer_welcome import WelcomeMessage  # isort:skip  # noqa: E402


def test_is_a_markdown():
    assert type(WelcomeMessage()) is WelcomeMessage


def test_contains_the_welcome_md_file(capsys):
    WelcomeMessage().print_welcome_message()
    out, err = capsys.readouterr()
    assert "Welcome to one-click-miniK8s" in out
