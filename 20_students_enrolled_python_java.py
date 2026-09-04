python_students = {"Pratik", "Amit", "Rahul", "Sneha"}
java_students = {"Rahul", "Sneha", "Pooja", "Rohan"}

both = python_students & java_students
only_one = python_students ^ java_students

print("Students in both courses:", both)
print("Students in only one course:", only_one)
