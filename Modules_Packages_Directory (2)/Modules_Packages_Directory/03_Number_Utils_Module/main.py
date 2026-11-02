# main.py - Use number_utils module
from number_utils import is_prime, is_palindrome, is_armstrong, is_perfect

n = int(input("Enter a number: "))
print(f"\n{n} is Prime     : {is_prime(n)}")
print(f"{n} is Palindrome: {is_palindrome(n)}")
print(f"{n} is Armstrong : {is_armstrong(n)}")
print(f"{n} is Perfect   : {is_perfect(n)}")
