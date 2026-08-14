scores = [45, 100, 75, 120, 50, 30, 80, 110, 60, 40]
highest = scores[0]
lowest = scores[0]
total = 0
centuries = 0
half_centuries = 0
for score in scores:
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score
    total = total + score
    if score >= 100:
        centuries = centuries + 1
    elif score >= 50:
        half_centuries = half_centuries + 1
average = total / 10
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total)
print("Average runs:", average)
print("Centuries:", centuries)
print("Half-centuries:", half_centuries)