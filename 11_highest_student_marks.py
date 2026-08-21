students = {"Pratik": 85, "Amit": 92, "Rahul": 78, "Sneha": 88}

highest_name = ""
highest_marks = -1

for name, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_name = name

print("Highest marks:", highest_name, highest_marks)
