numbers = [25, 10, 45, 5, 30]
largest = numbers[0]
smallest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
print("Largest:", largest)
print("Smallest:", smallest)