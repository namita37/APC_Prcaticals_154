filename = input("Enter file name: ")
with open(filename, "r") as file:
    text = file.read()
print("Total characters including spaces:", len(text))
