num = int(input("Enter a number: "))
i = 2
prime = True
if num <= 1:
    prime = False
else:
    while i <= num // 2:
        if num % i == 0:
            prime = False
            break
        i += 1
if prime:
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")
