def unique_elements(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result

def second_largest(lst):
    unique = unique_elements(lst)
    if len(unique) < 2:
        return None
    largest = second = None
    for x in unique:
        if largest is None or x > largest:
            second = largest
            largest = x
        elif second is None or x > second:
            second = x
    return second


print(second_largest([10, 20, 5, 20, 15]))
