def even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


print(even_numbers([1, 2, 3, 4, 5, 6]))
