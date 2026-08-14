numbers = [10, 20, 10, 30, 20, 10]
checked = []
for n in numbers:
    if n not in checked:
        count = 0
        for x in numbers:
            if x == n:
                count = count + 1
        print(n, "=", count)
        checked.append(n)