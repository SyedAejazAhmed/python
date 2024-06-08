n = int(input("enter a number:"))
m=int(n/2)
f=0
for i in range(2,m):
    if(n%i==0):
        print("Not a prime Number")
        f=1
        break
if f==0:
    print("prime Number")
