def electricity_bill(units):
    if units < 0:
        raise ValueError("units cannot be negative")
    if units <= 100:
        return units * 5
    if units <= 200:
        return 500 + (units - 100) * 7
    if units <= 300:
        return 1200 + (units - 200) * 10
    return 2200 + (units - 300) * 12


print(electricity_bill(250))
