def average(numbers):
    if not numbers:
        raise ValueError("numbers cannot be empty")
    return sum(numbers) / len(numbers)


print(average([10, 20, 30, 40]))
