print("Hello World")
print("*" * 10)

name = "John Smith"
age = 20 
new_patient = True

#name = input(" Enter name ? ")
#color = input( "Enter color? ")
#print(name + " favorite color is "+ color)

#weight = input(" Enter no of pounds: ")
#kilograms = int(weight) * 0.45
#print( kilograms)

#name = "Jeniffer"
#print(name.upper())
#print(name[1:-1])
#print(name[0:])
#print(name[:-1])

home_price = 1000000
is_good_credit = True
if is_good_credit:
    print(home_price * 0.10)
else:
    print(home_price * 0.20)
name = 123445
print(f"testing the name {name}")  

temperature = 30

if temperature > 30:
    print("its hot")
elif temperature < 30:
    print("its cold")
else: 
    print("its normal day")  

name = """

sdjfskldflsfjslkfklsjdksadfjsdlfsldfkjafkjsdjfsakjfsk
aljflsaslkfljskfkljasflkskjfjaslkjfaljfsjafsjl

"""

if len(name) < 3:
    print("name should not be less than 3")
elif len(name) > 50:
    print("name should not exceed 50 characters")
else:
    print("name looks good")

#weight = input("Weight: ")
#weight_mesurement = input("[L]bs or [K]gs: ")

#conversion_value = 0
#if weight_mesurement.lower() == "l":
#    conversion_value = int(weight) * 0.45
#else:
#    conversion_value = (int(weight) * 100) / 45

#print(conversion_value)    

#lucky_num = 9
#counter = 0

#while counter < 3:
#    num = input("Guess No : ")
#    counter = counter + 1
#    num = int(num)
#    if lucky_num == num :
#        print("You Win")
#        break
#else:
#    print("You reached maximum count")
#previous_command = ""
#while True:
#    command = input(">").lower()
#    if(previous_command == "start" and command == "start"):
#        print("GAME ALREADY STARTED")
#    elif(previous_command == "stop" and command == "stop"):
#        print("GAME ALREADY STOPPED")    

#    elif(command == "start"):
#        print("GAME STARTED")
#    elif(command == "stop"):
#        print("GAME STOPPED")
#    elif(command == "help"):
#        print(""" 
#        Start - Start the game
#        Stop - Stop the game
#        """)   
#    elif(command == "quit"):
#        break
#    else:
#        print("sorry I didn't understand the command") 
#    previous_command = command           

prices = [10,20, 30]
total_amount = 0
for price in prices:
    total_amount += price
print(f"Total amount is {total_amount}")    


for i in range(4):
    for j in range(4):
        print(f"({i}, {j})")

for i in [5, 2, 2, 5, 2, 2]:
      print("X"* i)      

input_array = [1,8,2,9,12,7,6]
largest_num = 0
for i in input_array:
    if i > largest_num:
        largest_num = i
print(largest_num)
#print(sort(input_array)[-1])              

matrix = [ 
   [1,2,3],
   [4,5,6],
   [7,8,9]
]

print(matrix[0][0])

for row in matrix:
    for item in row:
        print(item)

 #remove duplicates in list

input_nums = [1,2,3,4,5,6,1,2,3]
output_nums = []
for num in input_nums:
    if num not in output_nums:
        output_nums.append(num)
print(output_nums)  

num_words = {    
 "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9": "Nine"
}

#number = input("Enter:")
#words = ""
#for n in number:
#    print(n)
#    words += num_words.get(n, "!") + " "
#print(words)    

def square(number):
    return number * number

    
print(square(5))

def print_name(first_name,  last_name):
    print(f'Hi {first_name} {last_name}') 



print_name("Naveen", "Kumar")
print_name("fr", last_name="test" )
print_name(first_name="first", last_name="last")
