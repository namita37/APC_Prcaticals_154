def sort_students_by_marks(students):
    return sorted(students, key=lambda x: x[1])


print(sort_students_by_marks([('Asha', 85), ('Ravi', 72), ('Meera', 91)]))
