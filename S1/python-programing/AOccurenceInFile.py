import csv
count=0
with open(input("Enter the file:"),'r') as f:
    reader=csv.reader(f)
    for row in reader:
        for word in row:
          print(word,end=" ")
          for ch in word:
             if ch=='a':
                 count+=1
print(count)