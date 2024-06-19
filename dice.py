import random
class Dice:
    def roll(self):
        first_random = random.randint(0,9)
        second_random = random.randint(0,9)
        return first_random, second_random
