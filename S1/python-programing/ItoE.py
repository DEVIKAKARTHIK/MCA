import csv
with open(input("Enter the file:"),'r') as f:
    reader=csv.reader(f)
    for row in reader:
        for word in row:
            print(word,end=" ")
            newword=word.replace('e','i')
            print(newword,end=" ")