import pytest

from decode_morse import decode_morse


@pytest.mark.parametrize("morse_code, expected", [('.... . -.--   .--- ..- -.. .', 'HEY JUDE'), ('... --- ...', 'SOS')])
def test_morse_to_letter(morse_code, expected):
    result = decode_morse(morse_code)
    assert result == expected