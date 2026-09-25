# write a numpy program to save a given array  to a text file and load it
# np.savetext() used to store code in a text file
# loadtext() used to load 

import numpy as np

arr = np.array([1,3,4,5])

np.savetxt("ok.txt",arr,fmt="%d")


