# The copy owns the data and any changes made to the copy will not affect original array, 
# and any changes made to the original array will not affect the copy.

# The view does not own the data and any changes made to the view will affect the original 
# array, and any changes made to the original array will affect the view.

import numpy as np

array = np.array([1,2,3,4,5,6])
array_copy = array.copy()
array_view = array.view()

array_copy[0]=0
array_view[0]=123

print(array)

print(array_copy)

print(array_view)