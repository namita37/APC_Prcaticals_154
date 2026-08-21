paragraph = input("Enter a paragraph: ")
words = paragraph.split()
frequency = {}

for word in words:
    length = len(word)
    if length in frequency:
        frequency[length] += 1
    else:
        frequency[length] = 1

print(frequency)
