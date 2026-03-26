colors=[]
n=int(input("Enter the number of colors="))
for  i in  range(1,n+1):
    item=input("Enter the color=")
    colors.append(item)
print("First color=",colors[0])
print("Last color=",colors[-1])