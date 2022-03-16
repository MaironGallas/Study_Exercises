import pytest

from ten_minute_walk import is_valid_walk


@pytest.mark.parametrize('walk', [['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'], ['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w'],
                                  ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's']])
def test_valid_walk(walk):
    assert is_valid_walk(walk)


@pytest.mark.parametrize('walk', [['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e'], ['w'],['n','n','n','s','n','s','n','s','n','s']])
def test_not_valid_walk(walk):
    assert not is_valid_walk(walk)