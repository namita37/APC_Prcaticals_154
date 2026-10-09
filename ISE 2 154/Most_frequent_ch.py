s = input("Enter string: ")
max_count = 0
for ch in s:
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        result = ch
print(result)
