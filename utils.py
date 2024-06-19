
def find_max(numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max       

def find_min(numbers):
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num
    return min        

