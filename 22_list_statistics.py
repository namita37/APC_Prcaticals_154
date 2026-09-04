def average(numbers):
    if not numbers:
        raise ValueError("numbers cannot be empty")
    return sum(numbers) / len(numbers)

def list_statistics(numbers):
    return min(numbers), max(numbers), sum(numbers), average(numbers)


print(list_statistics([10, 20, 30, 40]))
