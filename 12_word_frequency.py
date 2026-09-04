import re

filename = input("Enter file name: ")
with open(filename, "r") as file:
    words = re.findall(r"\b\w+\b", file.read().lower())

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word frequency:", frequency)
