import numpy as np

array = np.array([1,3,4,5,6])

array_add = array + 1 #add one to array

print(f"add 1 to all elements of array-->{array_add}")

array_sub = array - 1 #add one to array

print(f"substract 1 to all elements of array-->{array_sub}")

array_mul = array * 3 #add one to array

print(f"multiply 3 to all elements of array-->{array_mul}")

array_div = array / 3 #add one to array

print(f"divide all elements of array by 3-->{array_div}")

for index, item in np.ndenumerate(array_div):
    print(f" index {index} item: {item}")