import shutil
import sys

import pytest

sys.path.append("./")  # noqa: E402
from modules.steps.step_brew import StepBrew  # isort:skip  # noqa: E402


def test_check_brew_is_installed():
    """🍺 expect to understand if the system has Brew installed"""
    assert type(StepBrew.is_brew_installed()) is bool


def test_stub_brew_is_installed(monkeypatch):
    """🍺 Stub 🎫 - expect that Brew is installed"""
    monkeypatch.setattr("shutil.which", lambda _: True)
    assert StepBrew.is_brew_installed() is True


def test_stub_brew_is_not_installed(monkeypatch):
    """🍺 Stub 🎫 - expect that Brew is NOT installed"""
    monkeypatch.setattr("shutil.which", lambda _: False)
    assert StepBrew.is_brew_installed() is False


def test_check_xcodebuild_is_installed():
    """🍺 expect to understand if the system has XCodeBuild installed"""
    assert type(StepBrew.is_xcodebuild_installed()) is bool


def test_stub_xcodebuild_is_installed(monkeypatch):
    """🍺 Stub 🎫 - expect that XCodeBuild is installed"""
    monkeypatch.setattr("shutil.which", lambda _: True)
    assert StepBrew.is_xcodebuild_installed() is True


def test_stub_xcodebuild_is_not_installed(monkeypatch):
    """🍺 Stub 🎫 - expect that XCodeBuild is NOT installed"""
    monkeypatch.setattr("shutil.which", lambda _: False)
    assert StepBrew.is_xcodebuild_installed() is False


def test_check_ruby_is_installed():
    """🍺 expect to understand if the system has ruby installed"""
    assert type(StepBrew.is_ruby_installed()) is bool


def test_stub_ruby_is_installed(monkeypatch):
    """🍺 Stub 🎫 - expect that Ruby is installed"""
    monkeypatch.setattr("shutil.which", lambda _: True)
    assert StepBrew.is_ruby_installed() is True


def test_stub_ruby_is_not_installed(monkeypatch):
    """🍺 Stub 🎫 - expect that Ruby is NOT installed"""
    monkeypatch.setattr("shutil.which", lambda _: False)
    assert StepBrew.is_ruby_installed() is False


def test_check_curl_is_installed():
    """🍺 expect to understand if the system has curl installed"""
    assert type(StepBrew.is_curl_installed()) is bool


def test_stub_curl_is_installed(monkeypatch):
    """🍺 Stub 🎫 - expect that curl is installed"""
    monkeypatch.setattr("shutil.which", lambda _: True)
    assert StepBrew.is_curl_installed() is True


def test_stub_curl_is_not_installed(monkeypatch):
    """🍺 Stub 🎫 - expect that curl is NOT installed"""
    monkeypatch.setattr("shutil.which", lambda _: False)
    assert StepBrew.is_curl_installed() is False


def test_install_brew(monkeypatch):
    """🍺 expect to install Brew 🍺 but it's yet installed"""
    monkeypatch.setattr(
        "modules.steps.step_brew.StepBrew.is_brew_installed", lambda: True
    )
    assert StepBrew.install_brew() == 0


def test_install_brew_but_missing_xcode(monkeypatch):
    """🍺 expect to install Brew 🍺 but the system is missing xcode"""
    monkeypatch.setattr(
        "modules.steps.step_brew.StepBrew.is_brew_installed", lambda: False
    )
    monkeypatch.setattr(
        "modules.steps.step_brew.StepBrew.is_xcodebuild_installed", lambda: False
    )
    assert StepBrew.install_brew() == "Error! The system is missing xcodebuild."


def test_install_brew_but_missing_core_components(monkeypatch):
    """🍺 expect to install Brew 🍺 but the system is missing ruby or curl"""
    monkeypatch.setattr(
        "modules.steps.step_brew.StepBrew.is_brew_installed", lambda: False
    )
    monkeypatch.setattr(
        "modules.steps.step_brew.StepBrew.is_xcodebuild_installed", lambda: True
    )
    monkeypatch.setattr(
        "modules.steps.step_brew.StepBrew.is_ruby_installed", lambda: False
    )
    monkeypatch.setattr(
        "modules.steps.step_brew.StepBrew.is_curl_installed", lambda: False
    )
    assert (
        StepBrew.install_brew()
        == "Error! The system is missing some core components: ruby or curl."
    )
