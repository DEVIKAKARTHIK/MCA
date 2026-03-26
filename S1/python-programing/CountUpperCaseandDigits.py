import csv
ucount=0
dcount=0
with open(input("Enter the file"),'r') as f:
    reader=csv.reader(f)
    for row in reader:
        for word in row:
            for ch in word:
              if ch.isupper():
                  ucount+=1
              if ch.isdigit():
                  dcount+=1
print("UpppercaseCount=",ucount)
print("Digitscount=",dcount)
                  
                 