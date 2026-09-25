#write a program to create a two-d array using numpy and print it


import numpy as np

arr1 = np.array([[1,2,3],[1,2,3],[5,6,7]])
arr2 = np.array([[1,2,3],[1,2,3],[5,6,7]])
c = arr1 + arr2
print("Sum = \n", c )
d = arr1 * arr2
print("product = \n", d)
e = np.dot (arr1,arr2)
print ("matrix multiplication= ",e)

print("transpose = ",np.transpose(arr2))
print("transpose = ",np.transpose(arr1))
