students = {
    "Pratik": "Computer Science",
    "Amit": "Mechanical",
    "Rahul": "Computer Science",
    "Sneha": "Electronics",
    "Pooja": "Mechanical"
}

departments = {}

for name, department in students.items():
    if department not in departments:
        departments[department] = []
    departments[department].append(name)

for department, names in departments.items():
    print(department, ":", names)
