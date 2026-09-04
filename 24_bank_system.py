balance = 0

transactions = []

def deposit(amount):
    global balance
    if amount <= 0:
        raise ValueError("deposit amount must be positive")
    balance += amount
    transactions.append(f"Deposited: {amount}")
    return balance

def withdrawal(amount):
    global balance
    if amount <= 0:
        raise ValueError("withdrawal amount must be positive")
    if amount > balance:
        return "Insufficient balance"
    balance -= amount
    transactions.append(f"Withdrawn: {amount}")
    return balance

def balance_enquiry():
    return balance

def transaction_history():
    return transactions


deposit(1000)
withdrawal(250)
print(balance_enquiry())
print(transaction_history())
