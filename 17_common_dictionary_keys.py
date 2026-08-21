dictionary1 = {"a": 10, "b": 20, "c": 30}
dictionary2 = {"b": 40, "c": 50, "d": 60}

common_keys = []

for key in dictionary1:
    if key in dictionary2:
        common_keys.append(key)

print("Common keys:", common_keys)
