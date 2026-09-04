file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")
output = input("Enter third/output file name: ")

with open(file1, "r") as f1, open(file2, "r") as f2:
    content = f1.read() + "\n" + f2.read()

with open(output, "w") as out:
    out.write(content)

print("Files merged successfully.")
