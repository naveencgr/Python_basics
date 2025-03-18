array_1 = [9,9,9,9,9,9,9,9]
array_2 = [9]

target_array = []

array1_len = len(array_1)
array2_len = len(array_2)

array1_index = array1_len - 1
array2_index = array2_len - 1
reminder = 0
carry = 0

while array1_index >= 0 or array2_index >= 0:
    print(f"{array1_index} {array2_index}")
    if array1_index >= 0 and array2_index >= 0:
        print("both are not zero")
        sum = carry + array_1[array1_index] + array_2[array2_index]
    elif array1_index < 0 and array2_index >= 0:
        print("array1 is zero")
        sum = carry + array_2[array2_index]
    elif array1_index >= 0 and array2_index < 0:
        print("array2 is zero")
        sum = carry + array_1[array1_index]
    else:
        sum = carry     
         
    print(sum)        
    if sum > 9:
        reminder = sum % 10
        carry = sum // 10
        target_array.append(reminder)
    else:
        target_array.append(sum)
        reminder = 0
        carry = 0   

    array2_index = array2_index - 1
    array1_index = array1_index - 1   

if carry != 0:
    target_array.append(carry)     

print(target_array)


