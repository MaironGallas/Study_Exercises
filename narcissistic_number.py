def narcissistic(value):
    return value == sum(map(lambda num: int(num)**len(str(value)), str(value)))
