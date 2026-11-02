# Module: student.py - Total marks, percentage, and grade

def total_marks(marks_list):
    """Calculate total marks from a list."""
    return sum(marks_list)

def percentage(marks_list, max_per_subject=100):
    """Calculate percentage."""
    total = total_marks(marks_list)
    maximum = max_per_subject * len(marks_list)
    return (total / maximum) * 100

def grade(pct):
    """Return grade based on percentage."""
    if pct >= 90: return "A+"
    elif pct >= 80: return "A"
    elif pct >= 70: return "B"
    elif pct >= 60: return "C"
    elif pct >= 50: return "D"
    else: return "F"
