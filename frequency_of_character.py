s = input("Enter a string: ")
target = input("Enter character to count: ")
count = 0
for ch in s:
    if ch == target:
        count += 1
print("Frequency of", target, "=", count)