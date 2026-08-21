students = {"Pratik": 85, "Amit": 90, "Rahul": 75}

while True:
    print("\n1. Add student")
    print("2. Update marks")
    print("3. Delete student")
    print("4. Search student")
    print("5. Display all students")
    print("6. Find highest marks")
    print("7. Calculate average")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added.")

    elif choice == 2:
        name = input("Enter student name: ")
        if name in students:
            students[name] = int(input("Enter new marks: "))
            print("Marks updated.")
        else:
            print("Student not found.")

    elif choice == 3:
        name = input("Enter student name: ")
        if name in students:
            del students[name]
            print("Student deleted.")
        else:
            print("Student not found.")

    elif choice == 4:
        name = input("Enter student name: ")
        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found.")

    elif choice == 5:
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == 6:
        if students:
            name = max(students, key=students.get)
            print("Highest marks:", name, students[name])
        else:
            print("No students.")

    elif choice == 7:
        if students:
            print("Average:", sum(students.values()) / len(students))
        else:
            print("No students.")

    elif choice == 8:
        break

    else:
        print("Invalid choice.")
