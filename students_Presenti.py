students = ["Rahul", "Amit", "Pratik", "Sneha"]
print("Total students:", len(students))
name = input("Enter student name: ")
if name in students:
    print("Student is present")
else:
    print("Student is absent")
students.append("Neha")
students.remove("Amit")
print("Updated students:", students)