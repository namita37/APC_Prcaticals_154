filename = input("Enter file name: ")
with open(filename, "r") as file:
    print("\nFile contents:\n")
    print(file.read())
