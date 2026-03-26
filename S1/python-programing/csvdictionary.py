import csv
dic={"first":"Harry","last":"Potter"}
with open("example.txt",'w') as f:
    writer=csv.writer(f)
    writer.writerow(dic.keys())
    writer.writerow(dic.values())
with open("example.txt",'r') as f:
    reader=csv.DictReader(f)
    for row in reader:
        print(row)


