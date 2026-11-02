# student/attendance.py - Attendance eligibility
def attendance_percentage(attended, total_classes):
    return (attended / total_classes) * 100

def is_eligible(attended, total_classes, threshold=75):
    return attendance_percentage(attended, total_classes) >= threshold
