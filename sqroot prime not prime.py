
num = 169 

sqrt_val = -1
for i in range(num + 1):
    if i * i == num:
        sqrt_val = i
        break
    elif i * i > num:
        break
if sqrt_val == -1:
    print(f"The number {num} does not have a whole number square root.")
else:
    is_prime = True
    
    if sqrt_val <= 1:
        is_prime = False
    else:
        for i in range(2, sqrt_val):
            if sqrt_val % i == 0:
                is_prime = False
                break

    if is_prime:
        print(f"The square root of {num} is {sqrt_val}, which IS a prime number.")
    else:
        print(f"The square root of {num} is {sqrt_val}, which is NOT a prime number.")
