# customers/profile.py
_customers = {}

def add_customer(cid, name, email):
    _customers[cid] = {"name": name, "email": email}
    print(f"Customer '{name}' added.")

def get_customer(cid):
    return _customers.get(cid)
