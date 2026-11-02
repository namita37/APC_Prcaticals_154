# products/inventory.py
from products.catalog import get_product

def update_stock(pid, qty):
    p = get_product(pid)
    if p: p["stock"] += qty

def check_stock(pid):
    p = get_product(pid)
    return p["stock"] if p else 0
