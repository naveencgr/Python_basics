import numpy as np

array = np.array([1,2,3,4,5,6])

print(array[1:5])

print(array[4:])

print(array[:4])

print(array[-3:-1])

print(array[1:5:2])

print(array[::2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

print(arr[0:2, 2])

print(arr[0:2, 1:4])