# main.py - College Project - Import from student and faculty packages
from student.details import get_student_details, display_student
from student.marks import calculate_result
from faculty.details import get_faculty_details, display_faculty

print("=== Student Information ===")
student = get_student_details("Alice", 101, "CS", 5)
display_student(student)
calculate_result(student["name"], [85, 90, 78, 92, 88])

print("\n=== Faculty Information ===")
faculty = get_faculty_details("Dr. Smith", "F001", "Computer Science", "Professor")
display_faculty(faculty)
