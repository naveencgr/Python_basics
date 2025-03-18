array =  [64, 34, 25, 12, 22, 11, 90, 5]
# Compare the first element with the next elements and replace 
# if element is greater
# Bubble up the value on each iteration
for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]

print(array)            