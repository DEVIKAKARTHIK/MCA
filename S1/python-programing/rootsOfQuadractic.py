import math
a=int(input("Enter a number="))
b=int(input("Enter a number="))
c=int(input("Enter a number="))
d=b**2-(4*a*c)
if d==0:
    print("One root exist:")
    root=-b/(2*a)
    print(root)
elif d>0:
    print("Two real roots exist:")
    root1=(-b+math.sqrt(d))/2*a
    root2=(-b-math.sqrt(d))/2*a
    print(root1,root2)
else:
    print("Two complex roots exist:")
    real=-b/(2*a)
    imag=(math.sqrt(-d))/2*a
    root1=complex(real,imag)
    root2=complex(real,-imag)
    print(root1,root2)

