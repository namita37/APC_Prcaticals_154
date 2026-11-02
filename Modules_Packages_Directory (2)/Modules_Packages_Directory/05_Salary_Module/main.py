# main.py - Use salary module
import salary

name  = input("Enter employee name: ")
basic = float(input("Enter basic salary : "))

gross = salary.gross_salary(basic)
deduc = salary.deductions(gross)
net   = salary.net_salary(basic)

print(f"\n=== Salary Slip for {name} ===")
print(f"Basic Salary : {basic:.2f}")
print(f"Gross Salary : {gross:.2f}")
print(f"Deductions   : {deduc:.2f}")
print(f"Net Salary   : {net:.2f}")
