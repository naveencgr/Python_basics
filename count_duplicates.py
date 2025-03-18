numbers = [1, 1, 2, 2 ,1 , 3 , 2, 2, 3]
num_set = set(numbers)
n = 1
result_val = dict.fromkeys(num_set, 0)

for num in num_set:
   result_val[num] = numbers.count(num)

def dict_val(x):
    return x[1]
print(result_val)

sorted_dict = sorted(result_val.items(), key = lambda x : x[1])

#sorted_dict.reverse()
print(sorted_dict)

print(sorted_dict[len(sorted_dict) - n][0])