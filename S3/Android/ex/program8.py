#numpy program to create a vector values from 0 to 20 and change the sign of the numbers in the range from 9 to 15

import numpy as np

arr=np.arange(21)

# arr[9:16] = np.negative(arr[9:16])

for i in arr:
    if(i >=9 and i<=15):
        arr[i] = i*-1
print(arr)
