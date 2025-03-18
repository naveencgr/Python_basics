array= [1,2,3,8,9]

target = 9 

for i in array:
    diff = target - i
    if diff in array:
        print(f"index1:{array.index(diff)} index2:{array.index(i)} ")
        break
