# import numpy as np

# arr = np.array([1,2,3,4,5,6])

# # ,[1,4,57,4,6,4]]

# print(arr)

# print(arr.shape)

# arr1 = arr.reshape(2,3)

# print(arr1.shape)

# arr = np.array([10,20,30,40])

# print(arr.shape)

# print(arr.reshape(4,1))
# print(arr.reshape(1,-1))

import numpy as np

newArr = np.array([10,20,30,40,50,60])

print(newArr.shape)

newArr1= newArr.reshape(1,-1)

print(newArr1)
print(newArr1.shape)

