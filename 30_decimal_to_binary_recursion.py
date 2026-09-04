def decimal_to_binary(n):
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 0:
        return "-" + decimal_to_binary(-n)
    if n < 2:
        return str(n)
    return decimal_to_binary(n // 2) + str(n % 2)


print(decimal_to_binary(25))
