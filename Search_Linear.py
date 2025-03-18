array = [1,2,3,4,5,6,8,7,10]

search_key = 7
found = False
target_index = -1
for i in range(len(array)):
    if array[i] == search_key:
        found = True
        target_index = i

if found:
    print(f"{search_key} found at index {target_index}")
else:   
    print(f"{search_key} not found")    