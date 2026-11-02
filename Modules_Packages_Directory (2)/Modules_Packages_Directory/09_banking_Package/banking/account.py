# banking/account.py - Account creation and balance management
accounts = {}

def create_account(acc_no, name, initial_balance=0):
    if acc_no in accounts:
        return f"Account {acc_no} already exists."
    accounts[acc_no] = {"name": name, "balance": initial_balance}
    return f"Account {acc_no} created for {name}."

def get_balance(acc_no):
    if acc_no not in accounts:
        return "Account not found."
    return accounts[acc_no]["balance"]
