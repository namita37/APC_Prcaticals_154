s = input("Enter a string: ")
frequency = {}
for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1
for ch, count in frequency.items():
    print(ch," appeard " ,count," times)
