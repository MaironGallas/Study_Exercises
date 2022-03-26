def tribonacci(signature, n):
    result = []
    if n == 0:
        return []

    for i in range(n):
        if i < 3:
            result.append(signature[i])
        else:
            result.append(result[i-1]+result[i-2]+result[i-3])

    return result
