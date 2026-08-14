numbers = []

for i in range(5):
    number = int(input("Enter number: "))
    numbers.append(number)

numbers_tuple = tuple(numbers)
print("Tuple:", numbers_tuple)
