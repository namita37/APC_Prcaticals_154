filename = input("Enter file name: ")
with open(filename, "r") as file:
    for line in file:
        print(line.rstrip())
