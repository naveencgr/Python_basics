array1 = [1, 3, 5]

array2 = [2, 4]

array1.extend(array2)

array1.sort()

print(array1)
median = 0
array_length = len(array1)
if array_length % 2 == 0:
    median = ( array1[array_length // 2] + array1[(array_length // 2 ) + 1] ) / 2
else:
    median = array1[array_length // 2]

print(median)        