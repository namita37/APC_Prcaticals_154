file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")

with open(file1, "r") as f1, open(file2, "r") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

if lines1 == lines2:
    print("Files are identical.")
else:
    print("Files are different.")
    max_lines = max(len(lines1), len(lines2))
    for i in range(max_lines):
        a = lines1[i].rstrip() if i < len(lines1) else "<no line>"
        b = lines2[i].rstrip() if i < len(lines2) else "<no line>"
        if a != b:
            print("First different line:", i + 1)
            print("File 1:", a)
            print("File 2:", b)
            break
