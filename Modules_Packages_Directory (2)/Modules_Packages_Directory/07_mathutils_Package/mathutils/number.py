# mathutils/number.py - Number classification functions
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def is_armstrong(n):
    digits = str(n)
    return sum(int(d)**len(digits) for d in digits) == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]
