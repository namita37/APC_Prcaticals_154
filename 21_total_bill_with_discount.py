def total_bill(prices, quantities, discount=10):
    if len(prices) != len(quantities):
        raise ValueError("prices and quantities must have the same length")
    if not 0 <= discount <= 100:
        raise ValueError("discount must be between 0 and 100")
    total = sum(price * quantity for price, quantity in zip(prices, quantities))
    return total * (1 - discount / 100)


print(total_bill([100, 200, 300], [2, 1, 3]))
