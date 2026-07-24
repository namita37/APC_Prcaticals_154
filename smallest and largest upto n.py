n = int(input("Enter the number of elements: "))
num = int(input("Enter number 1: "))
largest = smallest = num
count = 2
while count <= n:
    num = int(input(f"Enter number {count}: "))
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    count += 1
print("Largest number =", largest)
print("Smallest number =", smallest)
