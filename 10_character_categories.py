filename = input("Enter file name: ")
with open(filename, "r") as file:
    text = file.read()

alphabets = sum(ch.isalpha() for ch in text)
digits = sum(ch.isdigit() for ch in text)
spaces = sum(ch.isspace() for ch in text)
special = sum(not ch.isalnum() and not ch.isspace() for ch in text)

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)
