a=int(input("Enter a number"))
b=int(input("Enter a number"))
print("1:Add 2:Subtract 3:Multiply 4:Division")
choice=int(input("Enter the choice"))
if choice==1:
    print("Addition=",a+b)
elif choice==2:
    print("Subtraction=",a-b)
elif choice==3:
    print("Multiplication=",a*b)
elif choice==4:
    print("Division=",a/b)
