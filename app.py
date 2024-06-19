from utils import find_max, find_min
from ecommerce.sales import calc_sales
from dice import Dice

numbers = [2,3,4,5,11,3]
print(find_max(numbers))
print(find_min(numbers))
print(max(numbers))
print(min(numbers))

calc_sales()

dice_1 = Dice()
print(dice_1.roll())