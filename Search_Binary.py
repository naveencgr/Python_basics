array = [1,2,3,4,5,6,7,8,9,10, 15, 20, 25]

search_key = 21

def binary_search(array, low, high):
        
    if high >= low:
        mid = (low + high) // 2

        print(mid)

        if search_key == array[mid]:
            print(f"found at {array.index(search_key)}")
            return
        elif search_key < array[mid]:
            binary_search(array, low, mid -1)
        elif search_key > array[mid]:
            binary_search(array, mid  + 1, high)   
    else: 
        print("Not found")       
    
print(binary_search(array, 0, len(array)-1))

