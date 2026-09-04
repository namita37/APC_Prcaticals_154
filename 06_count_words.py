filename = input("Enter file name: ")
with open(filename, "r") as file:
    words = file.read().split()
print("Total words:", len(words))
