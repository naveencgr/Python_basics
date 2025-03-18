array =  [64, 34, 25, 12, 22, 11, 90, 5]

i = -1

def quickSort(array, start, end):
    if(end <= start):
        return
    i = start - 1
    pivot = array[end]
    for j in range(start, end):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[end] = array[end], array[i+1] 

    quickSort(array, start, i)
    quickSort(array, i+1, end )   

quickSort(array, 0, len(array) - 1)    
print(array)