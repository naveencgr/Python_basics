import random

names = ["a", "b", "c"]

print(random.choice(names))
for i in range(3):
    print(random.random())

for i in range(1):
    first_random_num = random.randint(0,9)
    second_random_num = random.randint(0,9)
    print(f"({first_random_num}, {second_random_num})")