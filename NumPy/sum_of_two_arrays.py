import numpy as np

array_1 = np.array([1,2,3,4,5,10])
array_2 = np.array([6,7,8,9,10,11])

print(f"sum of array --> {np.sum([array_1, array_2])}")

print(f"sum of array axis 0 --> {np.sum([array_1, array_2], axis=0)}")

print(f"sum of array axis 1 --> {np.sum([array_1, array_2], axis=1)}")