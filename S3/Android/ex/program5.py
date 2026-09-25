#create a numby program to create a element wise comparison of two arrays(>,<,>=,<=,=)

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([2, 2, 1, 5])

# print(a == b)

print(np.equal(a,b))

# print(np.not_equal(a,b))




