import numpy as np

array_1 = np.array([1,2,3,4,5])
array_2 = np.array([6,7,8,9,10])

print(f"vertical stack --> {np.vstack((array_1, array_2))}")

print(f" horizontal stack --> {np.hstack((array_1, array_2))}")

print(f" column stack --> {np.column_stack((array_1, array_2))}")