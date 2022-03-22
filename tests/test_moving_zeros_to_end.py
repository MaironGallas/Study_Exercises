import pytest

from moving_zeros_to_end import move_zeros


@pytest.mark.parametrize("array, expected", [([1, 2, 0, 1, 0, 1, 0, 3, 0, 1], [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]),
                                             ([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9],
                                              [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
def test_move_zeros(array, expected):
    result = move_zeros(array)
    assert result == expected