import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])

array_2d = array.reshape(9,2)

print(array_2d)

array_3d = array.reshape(3,3, 2)

print(array_3d)

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

array_4d = array.reshape(4, 1, 5)

print(array_4d)

array_4d = array.reshape(4,1, -1)

print(array_4d)

print(array_4d.base)

# Reshape always returns a view

#flatten the array
arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)