temperature = [
    30, 32, 31, 29, 35, 36, 34, 33, 31, 30,
    28, 29, 32, 34, 37, 38, 35, 33, 31, 30,
    29, 32, 34, 36, 37, 35, 33, 31, 30, 28
]
hottest = temperature[0]
coldest = temperature[0]
total = 0
for t in temperature:
    if t > hottest:
        hottest = t
    if t < coldest:
        coldest = t
    total = total + t
average = total / 30
above = 0
below = 0
for t in temperature:
    if t > average:
        above = above + 1
    elif t < average:
        below = below + 1
print("Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above)
print("Days below average:", below)