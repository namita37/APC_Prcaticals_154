filename = input("Enter file name: ")
with open(filename, "r") as file:
    text = file.read().lower()

vowels = sum(ch in "aeiou" for ch in text)
consonants = sum(ch.isalpha() and ch not in "aeiou" for ch in text)

print("Vowels:", vowels)
print("Consonants:", consonants)
