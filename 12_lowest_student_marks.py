students = {"Pratik": 85, "Amit": 92, "Rahul": 78, "Sneha": 88}

lowest_name = ""
lowest_marks = 101

for name, marks in students.items():
    if marks < lowest_marks:
        lowest_marks = marks
        lowest_name = name

print("Lowest marks:", lowest_name, lowest_marks)
