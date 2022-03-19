def binary_array_to_number(arr):
    return int(str(arr)[1:-1].replace(', ', ''), 2)
