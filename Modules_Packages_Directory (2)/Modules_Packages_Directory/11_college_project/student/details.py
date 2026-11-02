# student/details.py - Student details
def get_student_details(name, roll, branch, semester):
    return {"name": name, "roll": roll, "branch": branch, "semester": semester}

def display_student(student):
    print(f"  Name    : {student['name']}")
    print(f"  Roll No : {student['roll']}")
    print(f"  Branch  : {student['branch']}")
    print(f"  Semester: {student['semester']}")
