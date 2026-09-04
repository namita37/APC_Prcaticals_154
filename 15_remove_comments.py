source_name = input("Enter Python source file name: ")
output_name = input("Enter output file name: ")

with open(source_name, "r") as source, open(output_name, "w") as target:
    for line in source:
        stripped = line.lstrip()
        if not stripped.startswith("#"):
            target.write(line.split("#", 1)[0].rstrip() + "\n")

print("Single-line comments removed.")
