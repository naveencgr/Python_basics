num = 12321
num_str = str(num)
reverse_str = ""
for s in num_str:
    reverse_str = s + reverse_str

print(reverse_str)

if reverse_str == num_str:
    print("Palindrome")
else:
    print("Not a palindrome")    