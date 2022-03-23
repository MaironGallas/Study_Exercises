import pytest

from narcissistic_number import narcissistic


@pytest.mark.parametrize("value, expected", [(7, True), (371, True), (122, False)])
def test_narcissistic(value, expected):
    result = narcissistic(value)
    assert result == expected