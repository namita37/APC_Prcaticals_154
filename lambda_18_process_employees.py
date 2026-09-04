def process_employees(employees):
    above_50000 = list(filter(lambda x: x[2] > 50000, employees))
    increased = list(map(lambda x: (x[0], x[1], x[2] * 1.10), employees))
    sorted_employees = sorted(employees, key=lambda x: x[2])
    return above_50000, increased, sorted_employees


print(process_employees([('Asha', 'IT', 55000), ('Ravi', 'HR', 48000)]))
