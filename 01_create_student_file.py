name = input("Enter student name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

with open("student.txt", "w") as file:
    file.write(f"Name: {name}\nRoll Number: {roll}\nBranch: {branch}\nSemester: {semester}\n")

print("Student information saved.")
