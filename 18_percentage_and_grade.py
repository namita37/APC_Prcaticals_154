def percentage_grade(marks):
    if not marks:
        raise ValueError("marks cannot be empty")
    percentage = sum(marks) / len(marks)
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"
    return percentage, grade


print(percentage_grade([85, 90, 78, 88, 92]))
