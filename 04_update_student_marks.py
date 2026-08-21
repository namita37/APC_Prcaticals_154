students = {"Pratik": 85, "Amit": 75, "Rahul": 80}

name = input("Enter student name: ")
marks = int(input("Enter new marks: "))

if name in students:
    students[name] = marks
    print(students)
else:
    print("Student not found.")
