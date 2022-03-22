def move_zeros(array):
    return list(filter(lambda num: num != 0, array)) + [0] * array.count(0)

