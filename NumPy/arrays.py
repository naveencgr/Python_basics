import numpy as np

array = np.array([1,2,3,4,5,6])

print(array)
print(type(array))
print(array.shape)

array = np.array([[[1,2,3],[3,4,5],[5,6,7]]])

print(array)

print(array.ndim)
print(array.shape)

array = np.array([1,2,3,4,5], ndmin=5)

print(array)
