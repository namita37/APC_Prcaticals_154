# customers/auth.py
from customers.profile import get_customer

def validate_customer(cid):
    c = get_customer(cid)
    return f"Customer {cid} ({c['name']}) is valid." if c else "Invalid customer."
