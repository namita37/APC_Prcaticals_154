# Module: recursive_funcs.py - Recursive functions

def factorial(n):
    """Return factorial of n recursively."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Return nth Fibonacci number recursively."""
    if n <= 0: return 0
    if n == 1: return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def sum_of_digits(n):
    """Return sum of digits of n recursively."""
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)

def binary_conversion(n):
    """Convert decimal n to binary string recursively."""
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return binary_conversion(n // 2) + str(n % 2)
