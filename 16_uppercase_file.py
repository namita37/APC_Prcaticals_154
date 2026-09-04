source_name = input("Enter input file name: ")
output_name = input("Enter output file name: ")

with open(source_name, "r") as source, open(output_name, "w") as target:
    target.write(source.read().upper())

print("Uppercase file created.")
