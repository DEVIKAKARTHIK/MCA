#numpy program to create an array and to compute the sum of all the
#  elements and sum of each column and sum of each row

import numpy as np
arr=np.array([[1,3,4,5],[6,3,1,4],[5,6,8,6]])
print("sum of all elems: ",np.sum(arr))

print("sum of coumns: " ,np.sum(arr,axis=0))
print("sum of rows: " ,np.sum(arr,axis=1))