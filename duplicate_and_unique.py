numbers = [10, 20, 10, 30, 20, 40, 30]
unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)
print("Unique elements:", unique)