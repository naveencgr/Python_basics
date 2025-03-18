numbers_1 = [ 30, 31, 12, 12,13,19, 30,30,29, 29]

print(numbers_1[-2:])


numbers_set = set(numbers_1)

numbers_2 = [ 1,2,3,4,5, 19, 31]

print(numbers_set)
print(numbers_2)

symertric_diff = numbers_set.symmetric_difference(numbers_2)

print(symertric_diff)



diff_array =numbers_set.difference(numbers_2)
print(diff_array)

isSubSet = numbers_set.issuperset([29,32])

print(isSubSet)


print("Manually Done")

target_array = []

#target_array.extend(numbers_set)

print(target_array) 

for num in numbers_2:
    if num not in numbers_1 and num not in target_array:
        target_array.append(num)

for num in numbers_1:
    if num not in numbers_2 and num not in target_array:
        target_array.append(num)        

target_array.sort()
print(target_array)        

