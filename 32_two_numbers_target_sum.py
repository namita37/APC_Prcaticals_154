numbers = [2, 7, 11, 15, 3, 6]
target = int(input("Enter target value: "))

seen = {}

for number in numbers:
    required = target - number

    if required in seen:
        print("Numbers:", required, number)
        break

    seen[number] = True
else:
    print("No pair found.")
