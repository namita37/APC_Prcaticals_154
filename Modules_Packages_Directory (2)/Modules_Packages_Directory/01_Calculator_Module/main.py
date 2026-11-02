# main.py - Import calculator module and perform operations
import calculator

print("=== Calculator ===")
a = float(input("Enter first number : "))
b = float(input("Enter second number: "))

print(f"Addition       : {calculator.add(a, b)}")
print(f"Subtraction    : {calculator.subtract(a, b)}")
print(f"Multiplication : {calculator.multiply(a, b)}")
try:
    print(f"Division       : {calculator.divide(a, b)}")
except ValueError as e:
    print(f"Division Error : {e}")
