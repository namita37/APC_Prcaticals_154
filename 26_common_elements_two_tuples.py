tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)

common = tuple(set(tuple1) & set(tuple2))

print("Common elements:", common)
