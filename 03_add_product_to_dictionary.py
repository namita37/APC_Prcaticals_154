products = {"Pen": 10, "Book": 50, "Bag": 500, "Pencil": 5, "Bottle": 100}

product = input("Enter new product: ")
price = float(input("Enter price: "))

products[product] = price

print(products)
