# orders/cart.py
_carts = {}

def add_to_cart(cid, pid, qty=1):
    if cid not in _carts: _carts[cid] = []
    _carts[cid].append({"pid": pid, "qty": qty})

def view_cart(cid):
    print(f"\nCart for {cid}: {_carts.get(cid, [])}")

def get_cart(cid):
    return _carts.get(cid, [])
