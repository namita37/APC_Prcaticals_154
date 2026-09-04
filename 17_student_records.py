filename = input("Enter student records file name: ")

records = []
with open(filename, "r") as file:
    next(file)
    for line in file:
        roll, name, marks = line.strip().split(",")
        records.append((int(roll), name, float(marks)))

print("\nAll records:")
for r in records:
    print(r)

highest = max(records, key=lambda x: x[2])
print("\nHighest marks:", highest)

average = sum(r[2] for r in records) / len(records)
print("Average marks:", average)

print("\nStudents scoring more than 80:")
for r in records:
    if r[2] > 80:
        print(r)
