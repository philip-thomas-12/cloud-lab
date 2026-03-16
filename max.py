import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of cols: "))

print(f"Enter the matrix values ({cols} numbers per row, separated by spaces):")
matrix=[]
for i in range(rows):
    row=list(map(int,input().split()))
    matrix.append(row)
matrix=np.array(matrix)    

# Fixed the broken variable names here!
min_val = np.min(matrix)
max_val = np.max(matrix)

print("Min pooling:", min_val)
print("Max pooling:", max_val)