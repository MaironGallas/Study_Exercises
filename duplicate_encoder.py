def duplicate_encode(word):
    word_lower = word.lower()
    result = ""
    for letter in word_lower:
        if word_lower.count(letter) > 1:
            result += ')'
        else:
            result += '('
    return result
