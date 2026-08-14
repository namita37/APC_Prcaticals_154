employee_ids = (101, 102, 103, 104, 105)
employee_id = int(input("Enter employee ID: "))

if employee_id in employee_ids:
    print("Index:", employee_ids.index(employee_id))
else:
    print("Employee ID not found.")
