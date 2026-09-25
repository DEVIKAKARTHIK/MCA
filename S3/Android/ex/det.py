#find the determinant of matrix a
import numpy as np
from numpy import linalg 

arr1 = np.array([[1,2,3],[1,9,3],[5,6,7]])

print(linalg.det(arr1))
print(linalg.inv(arr1))

