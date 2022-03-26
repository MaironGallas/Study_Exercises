import pytest

from tribonacci_sequence import tribonacci


@pytest.mark.parametrize("signature, n, expected", [([1, 1, 1], 10, [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]),
                                                    ([0, 0, 1], 10, [0, 0, 1, 1, 2, 4, 7, 13, 24, 44])])
def test_sum_lowest(signature, n, expected):
    result = tribonacci(signature, n)
    assert result == expected