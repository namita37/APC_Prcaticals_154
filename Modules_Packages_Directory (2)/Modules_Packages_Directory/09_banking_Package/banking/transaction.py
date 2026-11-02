# banking/transaction.py - Deposit and withdrawal
from banking.account import accounts

def deposit(acc_no, amount):
    if acc_no not in accounts:
        return "Account not found."
    accounts[acc_no]["balance"] += amount
    return f"Deposited {amount}. New balance: {accounts[acc_no]['balance']}"

def withdraw(acc_no, amount):
    if acc_no not in accounts:
        return "Account not found."
    if accounts[acc_no]["balance"] < amount:
        return "Insufficient funds."
    accounts[acc_no]["balance"] -= amount
    return f"Withdrawn {amount}. New balance: {accounts[acc_no]['balance']}"
