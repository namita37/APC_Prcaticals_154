numbers = []
for i in range(10):
    n = int(input("Enter number: "))
    numbers.append(n)
sum = 0
for n in numbers:
    sum = sum + n
average = sum / 10
print("Sum:", sum)
print("Average:", average)