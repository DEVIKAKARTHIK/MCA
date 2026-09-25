#  read number of rows and columns
#  create matrix 1
#  read number of rows and columns for matrix 
#  cfeate matrix 2
#  find dot product then transpose of matrix 1 and matrix then trace of matrix 1 and 
#  find the rank of matrix1 and matrix2
#  find the determinant of matrix1
#  find the inverse of matrix 2

import numpy as np
print("matrix1= ")
rows = int(input("enter rows"))
cols = int(input("enter cols"))

arr =np.zeros((rows,cols),dtype=int)

for i in range(rows):
    for j in range(cols):
        arr[i][j] = int(input("enter value:"))
print("matrix2")
rows = int(input("enter rows"))
cols = int(input("enter cols"))

arr =np.zeros((rows,cols),dtype=int)

for i in range(rows):
    for j in range(cols):
        arr[i][j] = int(input("enter value:"))


print(arr)