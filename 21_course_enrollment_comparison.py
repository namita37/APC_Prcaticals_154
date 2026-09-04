python_students = {"Pratik", "Amit", "Rahul", "Sneha"}
java_students = {"Rahul", "Sneha", "Pooja", "Rohan"}

both = python_students.intersection(java_students)
only_one = python_students.symmetric_difference(java_students)

print("Students enrolled in both:", both)
print("Students enrolled in only one:", only_one)
