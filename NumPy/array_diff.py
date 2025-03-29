import numpy as np

array_1 = np.array([1,2,3,4,5,10])
array_2 = np.array([6,7,8,9,10])

print(f"unique elements in array_1 not in array_2 {np.setdiff1d(array_1, array_2)}")


print(f"unique elements in array_2 not in array_1 {np.setdiff1d(array_2, array_1)}")