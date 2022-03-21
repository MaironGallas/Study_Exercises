def solution(number):
    result = 0
    if number < 0:
        return result

    for n in range(0, number, 1):
        if not(n % 3) or not(n % 5):
            result += n

    return result
