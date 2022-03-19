import pytest

from duplicate_encoder import duplicate_encode


@pytest.mark.parametrize("word, expected", [("din", "((("), ("Success", ")())())"), ("@gFNQZjS(XOnpPTdKLodZBTSFD", '(())()()(())))))(()))())))')])
def test_new_phone_number(word, expected):
    result = duplicate_encode(word)
    assert result == expected