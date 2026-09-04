filename = input("Enter file name: ")
with open(filename, "r") as file:
    count = sum(1 for _ in file)
print("Total lines:", count)
