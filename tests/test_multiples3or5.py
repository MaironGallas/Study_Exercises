import pytest

from multiples_3_or_5 import solution


@pytest.mark.parametrize("number, expected", [(4, 3), (6, 8), (16, 60), (-1, 0)])
def test_new_phone_number(number, expected):
    result = solution(number)
    assert result == expected
