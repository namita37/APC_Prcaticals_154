# student/grade.py - Grade calculation
def get_grade(pct):
    if pct >= 90: return "A+"
    elif pct >= 80: return "A"
    elif pct >= 70: return "B"
    elif pct >= 60: return "C"
    elif pct >= 50: return "D"
    else: return "F"
