# List Comprehensions are very flexible. We even can expand our examples to incorporate conditional logic.

numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []

for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)

print(only_negative_doubled) 

# using comprehensions and conditional, the above becomes
# when using a single conditional, the for comes before the consitional
numbers = [2, -1, 79, 33, -45]
only_negative_doubled = [num * 2 for num in numbers if num < 0]

print(only_negative_doubled)

# in the above, the list comprehension
# Takes an element in the list numbers.
# Assigns that element to a variable called num.
# Checks if the condition num < 0 is met by the element stored in num. 
# If so, it goes to step 4, otherwise it skips it and goes to the next element in the list.
# Applies the expression num * 2 on the element stored in num and adds the result to a new list called negative_doubled
# Repeats steps 1-3 (and sometimes 4) for each remaining element in the numbers list.

#change the 
numbers = [22, 11, 79, 33, 45]
modulus_five = [num % 5 for num in numbers if num >= 0]
print(modulus_five)


# using if-Else condition
# when using if-Else the "for" comes after the If-Else conditional
numbers = [2, -1, 79, 33, -45]
doubled_or_tripled = [num * 2 if num < 0 else num * 3 for num in numbers ]
print(doubled_or_tripled)

#  list comprehension and conditionals
# numbers = [2, -1, 79, 33, -45]
# no_if   = [num * 2 for num in numbers]
# if_only = [num * 2 for num in numbers if num < 0]
# if_else = [num * 2 if num < 0 else num * 3 for num in numbers]

 
#   In order to ride the Topsy Turvy Tumbletron roller coaster, you need to be above 161 centimeters.
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [rider for rider in heights if rider > 161]
print(can_ride_coaster)