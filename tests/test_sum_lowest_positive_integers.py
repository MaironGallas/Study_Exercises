import pytest

from sum_two_lowest_positive_integers import sum_two_smallest_numbers


@pytest.mark.parametrize("numbers, expected", [([5, 8, 12, 18, 22], 13), ([7, 15, 12, 18, 22], 19)])
def test_sum_lowest(numbers, expected):
    result = sum_two_smallest_numbers(numbers)
    assert result == expected
