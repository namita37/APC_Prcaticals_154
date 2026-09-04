def count_occurrences(lst, element):
    count = 0
    for x in lst:
        if x == element:
            count += 1
    return count


print(count_occurrences([1, 2, 2, 3, 2], 2))
