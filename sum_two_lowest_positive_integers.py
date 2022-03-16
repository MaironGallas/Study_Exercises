def sum_two_smallest_numbers(numbers):
    list_positive_ordered = []
    list_ordered = sorted(numbers)
    for number in list_ordered:
        if number > 0:
            list_positive_ordered.append(number)

    return list_positive_ordered[0] + list_positive_ordered[1]