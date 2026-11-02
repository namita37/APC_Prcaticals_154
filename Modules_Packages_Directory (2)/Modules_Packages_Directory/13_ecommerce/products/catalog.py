# products/catalog.py
_products = {}

def add_product(pid, name, price, stock=0):
    _products[pid] = {"name": name, "price": price, "stock": stock}

def list_products():
    print("\n=== Products ===")
    for pid, p in _products.items():
        print(f"  ID:{pid} | {p['name']} | Price:{p['price']} | Stock:{p['stock']}")

def get_product(pid):
    return _products.get(pid)
