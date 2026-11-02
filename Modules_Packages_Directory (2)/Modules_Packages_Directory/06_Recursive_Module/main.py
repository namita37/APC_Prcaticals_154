# main.py - Use recursive_funcs module
from recursive_funcs import factorial, fibonacci, sum_of_digits, binary_conversion

n = int(input("Enter a number: "))
print(f"\nFactorial of {n}     : {factorial(n)}")
print(f"Fibonacci at {n}     : {fibonacci(n)}")
print(f"Sum of digits of {n} : {sum_of_digits(n)}")
print(f"Binary of {n}        : {binary_conversion(n)}")
