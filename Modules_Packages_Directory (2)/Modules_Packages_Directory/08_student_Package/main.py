# main.py - Student report using student package
from student.marks import total, percentage
from student.grade import get_grade
from student.attendance import attendance_percentage, is_eligible

name    = input("Enter student name: ")
n       = int(input("Enter number of subjects: "))
marks   = [float(input(f"  Subject {i+1} marks: ")) for i in range(n)]
attended = int(input("Classes attended: "))
total_cl = int(input("Total classes held: "))

tot  = total(marks)
pct  = percentage(marks)
grd  = get_grade(pct)
att  = attendance_percentage(attended, total_cl)
elig = is_eligible(attended, total_cl)

print(f"\n=== Report for {name} ===")
print(f"Total Marks      : {tot}")
print(f"Percentage       : {pct:.2f}%")
print(f"Grade            : {grd}")
print(f"Attendance       : {att:.2f}%")
print(f"Eligible for Exam: {'Yes' if elig else 'No'}")
