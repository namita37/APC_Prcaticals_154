text = input("Enter a string: ")
frequency = {}

for character in text:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

found = False

for character in text:
    if frequency[character] == 1:
        print("First non-repeating character:", character)
        found = True
        break

if not found:
    print("No non-repeating character.")
