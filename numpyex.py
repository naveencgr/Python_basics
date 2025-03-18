import numpy as np

print(np.__version__)

np_array = np.array([1,2,3,4])

print(np_array)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print(arr.ndim)