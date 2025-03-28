import numpy as np

array_1d = np.array([1,2,3,4,5,6,7])

for i in array_1d:
    print(i)

array_2d = np.array([[1,2,3],[4,5,6]])
for i in array_2d:
    for j in i:
        print(j) 

#In basic for loops, iterating through each scalar of an array 
# we need to use n for loops which can be difficult to write for 
# arrays with very high dimensionality.           

array = np.array([[[1,3,4,5,67],[1,2,3,4,5]],[[21,22,23,24,25],[221,222,223,224,225]],[[31,31,31,31,31],[32,32,32,32,32]]])

print(array)

for x in np.nditer(array):
    print(x)

#We can use op_dtypes argument and pass it the expected datatype to change the 
# datatype of elements while iterating.

#NumPy does not change the data type of the element in-place (where the element is in array) 
# so it needs some other space to perform this action, that extra space is called buffer, 
# and in order to enable it in nditer() we pass flags=['buffered'].
#     

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for i in np.nditer(arr[:,::2]):
    print(i)

for index, i in np.ndenumerate(arr):
    print(f"index -->{index}  i-->{i}")    
