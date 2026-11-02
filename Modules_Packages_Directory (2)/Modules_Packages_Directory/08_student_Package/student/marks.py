# student/marks.py - Total and percentage
def total(marks): return sum(marks)
def percentage(marks, max_per=100): return (total(marks) / (max_per * len(marks))) * 100
