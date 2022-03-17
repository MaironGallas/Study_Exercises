import pytest

from sum_of_numbers import get_sum


@pytest.mark.parametrize("a,b, expected", [(1, 0, 1), (1, 2, 3), (-1, 2, 2)])
def test_sum_numbers(a, b, expected):
    result = get_sum(a, b)
    assert result == expected
