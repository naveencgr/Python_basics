import numpy as np

array = np.array([1,2,3,4,5,6])

print(array[0])
print(array[len(array)-1])

print(array[1] + array[2])

array = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print(array[0,1])
print(array[1, 1])


array = np.array([[[1,2,3,4,5], [6,7,8,9,10]], [[11,12,13,14,15],[16,17,18,19,20]]])

print(array[1][1][3])

array = np.array([[1,2,3,4,5], [6,7,8,9,10]])

#negative indexing - last element from array

print(array[1, -1])