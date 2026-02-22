from login_button import LoginButton
import pytest


@pytest.fixture
def login_button():
    return LoginButton()


def test_name(login_button):
    assert login_button.get_label() == "Login"


def test_button_is_enabled_by_default(login_button):
    assert login_button.is_enabled() is True


def test_button_is_disabled(login_button):
    login_button.disable()
    assert login_button.is_enabled() is False


def test_button_status_on_or_off(login_button):
    login_button.disable()
    login_button.enable()
    assert login_button.is_enabled() is True
