import sys

import pytest
from rich.markdown import Markdown

sys.path.append("./")  # noqa: E402
from modules.installer_welcome import WelcomeMessage  # isort:skip  # noqa: E402


@pytest.fixture
def welcome_screen() -> WelcomeMessage:
    return WelcomeMessage()


def test_is_a_markdown(welcome_screen):
    assert type(welcome_screen.markdown) is Markdown


def test_contains_the_welcome_md_file(welcome_screen):
    assert "Welcome to one-click-miniK8s" in welcome_screen.markdown.markup
