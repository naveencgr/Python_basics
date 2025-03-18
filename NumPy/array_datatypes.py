import numpy as np

array = np.array([1,2,3,4,5])
print(array.dtype)

array = np.array([1,2,3,4,5], dtype="S")
print(array.dtype)

array = np.array([1.1,2.2,3.3])
print(array.dtype)
result = array.astype('i')
print(result.dtype)

result = array.astype(int)
print(result.dtype)

result_bool = array.astype(bool)
print(result_bool)
print(result_bool.dtype)