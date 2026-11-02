# main.py - Use mathutils package
from mathutils.basic import add, subtract, multiply, divide
from mathutils.number import is_prime, is_armstrong, is_palindrome
from mathutils.statistics import mean, maximum, minimum

print("=== Basic Operations ===")
print(f"10 + 5 = {add(10, 5)}")
print(f"10 - 5 = {subtract(10, 5)}")
print(f"10 * 5 = {multiply(10, 5)}")
print(f"10 / 5 = {divide(10, 5)}")

print("\n=== Number Functions ===")
n = int(input("Enter a number: "))
print(f"Is Prime     : {is_prime(n)}")
print(f"Is Armstrong : {is_armstrong(n)}")
print(f"Is Palindrome: {is_palindrome(n)}")

print("\n=== Statistics ===")
data = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"Mean    : {mean(data):.2f}")
print(f"Maximum : {maximum(data)}")
print(f"Minimum : {minimum(data)}")
