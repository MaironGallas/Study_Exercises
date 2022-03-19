import pytest

from ones_and_zeros import binary_array_to_number


@pytest.mark.parametrize("arr, expected", [([0, 0, 0, 1], 1), ([0, 1, 1, 0], 6)])
def test_new_phone_number(arr, expected):
    result = binary_array_to_number(arr)
    assert result == expected