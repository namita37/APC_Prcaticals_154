def largest_element(numbers):
    if not numbers:
        raise ValueError("numbers cannot be empty")
    largest = numbers[0]
    for value in numbers[1:]:
        if value > largest:
            largest = value
    return largest


print(largest_element([10, 25, 7, 40, 15]))
