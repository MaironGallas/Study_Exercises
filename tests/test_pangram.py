import pytest

from detect_pangram import is_pangram


@pytest.mark.parametrize("pangram, expected", [("The quick, brown fox jumps over the lazy dog!", True), ("The quic, brown fox jumps over the lazy dog!", False)])
def test_new_phone_number(pangram, expected):
    result = is_pangram(pangram)
    assert result == expected
