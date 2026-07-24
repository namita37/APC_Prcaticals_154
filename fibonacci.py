n= int(input("enter a number"))
i=0
fno=0
sno=1
print(fno)
print(sno)
while(i<=n):
    tno=fno+sno
    print(tno)
    i+=1
    fno=sno
    sno=tno
