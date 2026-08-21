dictionary1 = {"a": 10, "b": 20, "c": 30}
dictionary2 = {"x": 20, "y": 40, "z": 30}

common_values = []

for value in dictionary1.values():
    if value in dictionary2.values() and value not in common_values:
        common_values.append(value)

print("Common values:", common_values)
