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

def student_records(students):
    if not students:
        raise ValueError("students cannot be empty")
    results = []
    for name, roll, marks in students:
        total = sum(marks)
        percentage, grade = percentage_grade(marks)
        results.append((name, roll, marks, total, percentage, grade))
    class_average = sum(result[4] for result in results) / len(results)
    return results, class_average, max(results, key=lambda result: result[4]), min(results, key=lambda result: result[4])


print(student_records([('Asha', 1, [80, 85, 90]), ('Ravi', 2, [70, 75, 80])]))
