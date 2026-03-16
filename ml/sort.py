import csv

with open ("data.csv") as f:
    reader=csv.reader(f)
    header=next(reader)
    data=list(reader)

data.sort(key=lambda x:int(x[1]))    

print (header)

for row in data:
   print (row)