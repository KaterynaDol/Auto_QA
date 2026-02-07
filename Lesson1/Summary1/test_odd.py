from odd import EvenOddChecker
import pytest


@pytest.fixture
def even_odd_checker():
    return EvenOddChecker()


def test_is_even(even_odd_checker):
    assert even_odd_checker.is_even(2) is True
    assert even_odd_checker.is_even(3) is False
    assert even_odd_checker.is_even(-2) is True


def test_is_odd(even_odd_checker):
    assert even_odd_checker.is_odd(2) is False
    assert even_odd_checker.is_odd(3) is True
    assert even_odd_checker.is_odd(-2) is False