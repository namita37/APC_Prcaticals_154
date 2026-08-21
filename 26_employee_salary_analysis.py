employees = {
    "Amit": 45000,
    "Rahul": 60000,
    "Sneha": 75000,
    "Pooja": 50000
}

highest = max(employees.values())
lowest = min(employees.values())
average = sum(employees.values()) / len(employees)

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)

print("Employees earning more than 50000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)
