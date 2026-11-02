# Module: number_utils.py - Number checks

def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    """Return True if n is a palindrome."""
    return str(n) == str(n)[::-1]

def is_armstrong(n):
    """Return True if n is an Armstrong number."""
    digits = str(n)
    power  = len(digits)
    return sum(int(d) ** power for d in digits) == n

def is_perfect(n):
    """Return True if n is a perfect number."""
    if n < 1: return False
    return sum(i for i in range(1, n) if n % i == 0) == n
