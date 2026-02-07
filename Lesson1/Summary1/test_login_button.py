from login_button import LoginButton
import pytest


@pytest.fixture
def login_button():
    return LoginButton()

def test_name(login_button):
    assert login_button.get_label() == "Login"
