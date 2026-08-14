list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]
common = []
for n in list1:
    if n in list2:
        common.append(n)
print("Common elements:", common)