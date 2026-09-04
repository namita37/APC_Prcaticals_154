filename = input("Enter input file name: ")
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")
output = input("Enter output file name: ")

with open(filename, "r") as file:
    text = file.read()

text = text.replace(old_word, new_word)

with open(output, "w") as file:
    file.write(text)

print("Modified text saved in", output)
