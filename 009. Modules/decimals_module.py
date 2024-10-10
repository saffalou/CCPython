# Import Decimal below:
from decimal import Decimal
# without using Decimal
dec1 = 0.2
dec2 = 0.69
dectot = dec1 +dec2

print(dectot)


dec3 = 0.53
dec4 = 0.65
dectota = dec3 * dec4

print(dectota)

# Fix the floating point math below:
decimal_one = Decimal('0.2')
decimal_two = Decimal('0.69')
two_decimal_points = decimal_one + decimal_two
print(two_decimal_points)


decimal_three = Decimal('0.53')
decimal_four = Decimal('0.65')

four_decimal_points =  decimal_three * decimal_four
print(four_decimal_points)
