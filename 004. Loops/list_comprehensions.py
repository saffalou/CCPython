#  let’s say we had a list of integers and wanted to create a list where each element is doubled. 
# We could accomplish this using a for loop and a new list called doubled:
numbers = [2, -1, 79, 33, -45]
doubled = []

for number in numbers:
  doubled.append(number * 2)

print(doubled)

# using list comprehension the above becomes
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)

# a breakdown of the above
# new_list = [<expression> for <element> in <collection>]

# In our doubled example, our list comprehension:
# Takes an element in the list numbers
# Assigns that element to a variable called num (our <element>)
# Applies the <expression> on the element stored in num and adds the result to a new list called doubled
# Repeats steps 1-3 for every other element in the numbers list (our <collection>)


# Using a list comprehension, create a new list called scaled_grades that scales the class grades based on the highest score.
# Since the highest score was a 90 we simply want to add 10 points to all the grades in the list.

grades = [90, 88, 62, 76, 74, 89, 48, 57]

scaled_grades =[marks + 10 for marks in grades]

print(scaled_grades)