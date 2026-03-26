def fibanacci(n):
    if n<=1:
        return n
    else:
        return fibanacci(n-1)+fibanacci(n-2)
n=int(input("enter a number="))
lis=[]
print("fibonacci series=")
for i in range(n+1):
    lis.append(fibanacci(i))
print(lis)



a=0
b=1

for i in range(4):
    print(a,end=" ")
    a,b=b,a+b
 