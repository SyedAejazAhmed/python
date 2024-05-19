num = int(input("Enter a Number:"))
sum = 0
temp = num
s= num
n=0
while(s>0):
    s=s//10
    n+=1
while(num>0):
    rem = num%10
    sum = sum + rem**n
    num = num//10
if (temp == sum):
    print("%d is an Armstring number"%(sum))
else:
    print("%d is not an Armstrong Number"%(sum))
