def process_students_lambda(students):
    if not students:
        raise ValueError("students cannot be empty")
    avg = sum(mark for _, mark in students) / len(students)
    above_75 = list(filter(lambda student: student[1] > 75, students))
    return avg, above_75, sorted(students, key=lambda student: student[1])


print(process_students_lambda([('Asha', 85), ('Ravi', 72), ('Meera', 91)]))
