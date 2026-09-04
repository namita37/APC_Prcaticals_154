filename = input("Enter employee file name: ")

def read_employees():
    employees = []
    with open(filename, "r") as file:
        for line in file:
            emp_id, name, dept, salary = line.strip().split(",")
            employees.append((int(emp_id), name, dept, float(salary)))
    return employees

def display_all():
    for e in read_employees():
        print(e)

def highest_paid():
    return max(read_employees(), key=lambda e: e[3])

def average_salary():
    employees = read_employees()
    return sum(e[3] for e in employees) / len(employees)

def above_salary(amount):
    return [e for e in read_employees() if e[3] > amount]

print("All employees:")
display_all()
print("Highest-paid employee:", highest_paid())
print("Average salary:", average_salary())

limit = float(input("Enter salary limit: "))
print("Employees earning above the limit:")
for e in above_salary(limit):
    print(e)
