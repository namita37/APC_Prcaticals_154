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

def modular_electricity_bill(units):
    energy = electricity_bill(units)
    fixed_charge = 100
    tax = (energy + fixed_charge) * 0.05
    discount = 0.10 * energy if units < 100 else 0
    return energy + fixed_charge + tax - discount


print(modular_electricity_bill(250))
