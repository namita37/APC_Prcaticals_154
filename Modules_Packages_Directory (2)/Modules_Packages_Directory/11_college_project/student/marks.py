# student/marks.py - Marks and result
def calculate_result(name, marks):
    total = sum(marks)
    pct   = total / (100 * len(marks)) * 100
    grade = "A" if pct >= 80 else "B" if pct >= 70 else "C" if pct >= 60 else "F"
    print(f"  {name}'s Total: {total}, Percentage: {pct:.2f}%, Grade: {grade}")
