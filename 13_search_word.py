filename = input("Enter file name: ")
word = input("Enter word to search: ").lower()

total = 0
line_numbers = []

with open(filename, "r") as file:
    for number, line in enumerate(file, start=1):
        words = line.lower().split()
        count = words.count(word)
        if count:
            total += count
            line_numbers.append(number)

print("Occurrences:", total)
print("Line numbers:", line_numbers)
