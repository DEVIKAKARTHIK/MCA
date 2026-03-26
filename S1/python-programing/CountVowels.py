import csv
occ={}
count=0
with open(input("Enter the file:"),'r') as f:
    reader=csv.reader(f)
    for row in reader:
        for word in row:
            for ch in word :
               if ch in 'AEIOUaeiou':
                  count+=1
                  occ[ch]=occ.get(ch,0)+1
print("Occurences=",occ)
print("count",count)
