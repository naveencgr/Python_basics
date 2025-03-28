import numpy as np

array = np.array([1,2,4,5,6,7,8,9])

result = np.where(array == 5)
print(result)

result = np.where(array % 2 == 0)
print(result)

#The searchsorted() method is assumed to be used on sorted arrays.
# The method starts the search from the left and returns the first index 
# where the number 7 is no longer larger than the next value.
result = np.searchsorted(array, 7)
print(result)

result = np.searchsorted(array, 3)
print(result)

result = np.searchsorted(array, [5,10,2])
print(result)

result = np.searchsorted(array, 3, side='right')
print(result)