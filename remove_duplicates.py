numbers = [10, 20, 10, 30, 20, 40, 30]
new_list = []
for n in numbers:
    if n not in new_list:
        new_list.append(n)
print("List after removing duplicates:", new_list)