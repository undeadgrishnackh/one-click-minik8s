import pytest
from rich.markdown import Markdown
import sys
from src.welcome import Welcome

@pytest.fixture
def welcome_screen():
    return Welcome()


def test_is_a_markdown(welcome_screen):
    assert type(welcome_screen.markdown) is Markdown
    
    
def test_contains_the_welcome_md_file(welcome_screen):
    assert "Welcome to one-click-miniK8s" in welcome_screen.markdown.markup