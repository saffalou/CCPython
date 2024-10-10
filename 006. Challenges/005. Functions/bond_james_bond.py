# Write a function named introduction() that has two parameters named first_name and last_name.
# The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name.
def introduction(first_name, last_name):
    spy = last_name + ", " + first_name + " " + last_name
    return spy


# should print Bond, James Bond
print(introduction("James", "Bond"))

# should print Angelou, Maya Angelou
print(introduction("Maya", "Angelou"))

