def greater_than_50(numbers):
    return list(filter(lambda x: x > 50, numbers))


print(greater_than_50([20, 55, 75, 40]))
