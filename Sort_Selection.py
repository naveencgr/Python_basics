array =  [64, 34, 25, 12, 22, 11, 90, 5]
#Selection sort - Find minimum
#Find minimum value in each iteration and insert that to an array
for i in range(len(array)):
    min_index = i 
    for j in range(i+1, len(array)):
        if array[j] < array[min_index]:
            min_index = j
    value = array.pop(min_index)
    array.insert(i, value)
    print(array)

print(array)