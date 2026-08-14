marks = [50, 60, 70, 80, 90, 55, 65, 75, 85, 95,
         45, 58, 68, 78, 88, 92, 62, 72, 82, 40]
highest = marks[0]
lowest = marks[0]
total = 0
for m in marks:
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m
    total = total + m
average = total / 20
above = 0
below = 0
for m in marks:
    if m > average:
        above = above + 1
    elif m < average:
        below = below + 1
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
print("Above average:", above)
print("Below average:", below)