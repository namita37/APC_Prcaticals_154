def process_products(products):
    values = list(map(lambda x: (x[0], x[1] * x[2]), products))
    above_1000 = list(filter(lambda x: x[1] > 1000, values))
    sorted_products = sorted(values, key=lambda x: x[1])
    return values, above_1000, sorted_products


print(process_products([('Book', 200, 6), ('Pen', 20, 10)]))
