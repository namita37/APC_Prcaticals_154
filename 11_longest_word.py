import re

filename = input("Enter file name: ")
with open(filename, "r") as file:
    words = re.findall(r"[A-Za-z0-9]+", file.read())

if words:
    print("Longest word:", max(words, key=len))
else:
    print("No words found.")
