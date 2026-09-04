filename = input("Enter file name: ")
with open(filename, "r") as file:
    lines = file.readlines()

print("Lines in reverse order:")
for line in reversed(lines):
    print(line.rstrip())
