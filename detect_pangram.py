import string


def is_pangram(pangram):
    return not set(string.ascii_lowercase) - set(pangram.lower())
