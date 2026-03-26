import csv
with open(input("Enter the filename:"),'r') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
