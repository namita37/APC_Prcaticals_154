employee = {"id": 101, "name": "Amit", "department": "IT", "salary": 45000}

key = input("Enter key: ")

if key in employee:
    print("Value:", employee[key])
else:
    print("Key not found.")
