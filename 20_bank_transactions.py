filename = input("Enter transaction file name: ")

deposits = 0
withdrawals = 0
balance = 0
largest = 0

with open(filename, "r") as file:
    for line in file:
        kind, amount = line.strip().split(",")
        amount = float(amount)
        largest = max(largest, amount)

        if kind.upper() == "D":
            deposits += amount
            balance += amount
        elif kind.upper() == "W":
            withdrawals += amount
            balance -= amount

print("Total deposits:", deposits)
print("Total withdrawals:", withdrawals)
print("Final balance:", balance)
print("Largest transaction:", largest)
