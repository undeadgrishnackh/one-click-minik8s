import sys

import pytest

sys.path.append("./")  # noqa: E402
from modules.installer_title import Title  # isort:skip  # noqa: E402


def test_is_a_markdown():
    assert type(Title()) is Title


def test_contains_the_welcome_md_file(capsys):
    Title().print_welcome_message()
    out, err = capsys.readouterr()
    assert "Welcome to one-click-miniK8s" in out
