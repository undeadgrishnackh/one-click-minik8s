import sys

import pytest
from rich.markdown import Markdown

from src.console_markdown_welcome import Welcome


@pytest.fixture
def welcome_screen():
    return Welcome()


def test_is_a_markdown(welcome_screen):
    assert type(welcome_screen.markdown) is Markdown


def test_contains_the_welcome_md_file(welcome_screen):
    assert "Welcome to one-click-miniK8s" in welcome_screen.markdown.markup