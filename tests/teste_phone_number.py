import pytest

from phone_number import create_phone_number


@pytest.mark.parametrize("n, expected", [([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "(123) 456-7890"), ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], "(111) 111-1111")])
def test_new_phone_number(n, expected):
    result = create_phone_number(n)
    assert result == expected
