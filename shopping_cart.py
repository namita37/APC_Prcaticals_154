cart = ["Pen", "Book", "Bag","Pencil","Notebook","Marker","Ruler","Eraser","Glue","Scissors"]
cart.append("Pencil")
cart.remove("Pen")
item = "Book"
if item in cart:
    print("Item found")
else:
    print("Item not found")
print("Shopping cart:", cart)
print("Total items:", len(cart))