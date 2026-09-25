
#create a 5*5 zero matrix on the and  diagonal = 1,2,3,4,5 should appear


import numpy as np

arr = np.diag(np.arange(1,6))

# for i in range(arr.size):
#     for j in range(arr.size):
#         if(i==j):
#             print(arr[i][j])


print(arr)