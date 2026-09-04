numbers = {10, 20, 30, 40, 50}

number = int(input("Enter number to remove: "))

if number in numbers:
    numbers.remove(number)
    print(numbers)
else:
    print("Number not found.")
