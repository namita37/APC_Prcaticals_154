def sort_employees_by_salary(employees):
    return sorted(employees, key=lambda x: x[1])


print(sort_employees_by_salary([('Asha', 55000), ('Ravi', 48000), ('Meera', 62000)]))
