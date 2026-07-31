n=int(input("Enter a number :"))
fact=1
sum=1
for i in range(1, n):
    fact = fact * i
    sum += 1/fact

print("The sum of the factorials is:", sum)
