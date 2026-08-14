numbers = (10, 20, 30, 40)

number_list = list(numbers)
number_list[1] = 200

numbers = tuple(number_list)

print("Modified tuple:", numbers)
