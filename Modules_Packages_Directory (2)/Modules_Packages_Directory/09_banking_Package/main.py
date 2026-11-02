# main.py - Banking package demo
from banking.account import create_account, get_balance
from banking.transaction import deposit, withdraw
from banking.loan import calculate_emi, total_payment

print(create_account("ACC001", "Alice", 1000))
print(create_account("ACC002", "Bob",   500))

print(deposit("ACC001", 2000))
print(withdraw("ACC001", 500))
print(f"Balance of ACC001: {get_balance('ACC001')}")

principal = float(input("\nEnter loan principal: "))
rate      = float(input("Enter annual interest rate (%): "))
months    = int(input("Enter loan tenure (months): "))
emi       = calculate_emi(principal, rate, months)
print(f"Monthly EMI    : {emi}")
print(f"Total Payment  : {total_payment(emi, months)}")
