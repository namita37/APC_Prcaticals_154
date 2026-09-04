def add_product(cart, name, price, quantity):
    cart.append({"name": name, "price": price, "quantity": quantity})

def remove_product(cart, name):
    cart[:] = [p for p in cart if p["name"] != name]

def subtotal(cart):
    return sum(p["price"] * p["quantity"] for p in cart)

def apply_coupon(amount, coupon):
    if coupon == "SAVE10":
        return amount * 0.90
    if coupon == "SAVE20":
        return amount * 0.80
    return amount

def calculate_gst(amount, rate=18):
    return amount * rate / 100

def final_invoice(cart, coupon=None):
    sub = subtotal(cart)
    discounted = apply_coupon(sub, coupon)
    gst = calculate_gst(discounted)
    return discounted + gst


cart = []
add_product(cart, 'Notebook', 50, 4)
add_product(cart, 'Pen', 10, 3)
print(final_invoice(cart, 'SAVE10'))
