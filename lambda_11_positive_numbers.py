def positive_numbers(numbers):
    return list(filter(lambda x: x > 0, numbers))


print(positive_numbers([-2, 5, -1, 8]))
