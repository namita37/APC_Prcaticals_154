filename = input("Enter file name: ")
info = input("Enter additional information: ")

with open(filename, "a") as file:
    file.write(info + "\n")

print("Information appended successfully.")
