numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
even = 0
odd = 0
for n in numbers:
    if n % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print("Even numbers:", even)
print("Odd numbers:", odd)