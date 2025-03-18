array =  [64, 34, 25, 12, 22, 11, 90, 5]
# Insertion - checking previous elements
#Start with second element and compare with previou element
# If previous is greater than current element insert that to array 
for i in range(1, len(array)):
    index = i
    value = array.pop(index)
    for j in range(i-1, -1, -1):
        if array[j] > value:
            index = j

    array.insert(index, value)
    print(array)

print(array)    