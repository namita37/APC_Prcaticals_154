# main.py - Generate student result using student module
import student

name = input("Enter student name: ")
n    = int(input("Enter number of subjects: "))
marks = []
for i in range(n):
    m = float(input(f"  Marks for subject {i+1}: "))
    marks.append(m)

total = student.total_marks(marks)
pct   = student.percentage(marks)
grd   = student.grade(pct)

print(f"\n=== Result for {name} ===")
print(f"Total Marks : {total}")
print(f"Percentage  : {pct:.2f}%")
print(f"Grade       : {grd}")
