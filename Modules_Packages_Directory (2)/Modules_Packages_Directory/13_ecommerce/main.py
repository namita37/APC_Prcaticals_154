# main.py - E-Commerce Application
from products.catalog import add_product, list_products
from products.inventory import update_stock, check_stock
from customers.profile import add_customer, get_customer
from customers.auth import validate_customer
from orders.cart import add_to_cart, view_cart
from orders.order_manager import place_order
from payments.process import process_payment
from payments.refund import process_refund

# Products
add_product(1, "Laptop",    65000, stock=10)
add_product(2, "Mouse",       500, stock=50)
add_product(3, "Keyboard",   1200, stock=30)
list_products()

# Customers
add_customer("C001", "Alice", "alice@example.com")
print(validate_customer("C001"))

# Cart and Order
add_to_cart("C001", 1, qty=1)
add_to_cart("C001", 2, qty=2)
view_cart("C001")
order_id = place_order("C001")

# Payment
print(process_payment(order_id, "C001", method="UPI"))
print(process_refund(order_id, reason="Wrong item"))
