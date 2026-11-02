# orders/order_manager.py
from orders.cart import get_cart
from products.catalog import get_product

_orders = {}
_order_counter = [1]

def place_order(cid):
    cart = get_cart(cid)
    total = sum(get_product(item["pid"])["price"] * item["qty"] for item in cart)
    oid = f"ORD{_order_counter[0]:03d}"
    _orders[oid] = {"customer": cid, "items": cart, "total": total, "status": "Placed"}
    _order_counter[0] += 1
    print(f"Order {oid} placed. Total: {total}")
    return oid
