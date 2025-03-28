import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9])

array_split = np.split(array, 3)
print(array_split)

array_split = np.array_split(array, 3)
print(array_split)

array_concat = np.concatenate((array,np.array([2])))

array_split = np.array_split(array_concat, 3)
print(array_split)

array_split = np.split(array_concat, 3)
print(array_split)
