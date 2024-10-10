# this code returns an error
# Because the indices start at 0, so the final character in favorite_fruit has an index of 8. len(favorite_fruit) returns 9
#  and, because there is no value at that index, an IndexError occurs.

# favorite_fruit = "blueberry"

# last_char = favorite_fruit[len(favorite_fruit)]

# print(last_char)

# this code does the same thing without throwing an error
# output = y
favorite_fruit = "blueberry"
last_char = favorite_fruit[len(favorite_fruit) - 1]

print(last_char)

# we can also slice like this
# Output: erry
length = len(favorite_fruit)
last_chars = favorite_fruit[length - 4:]
print(last_chars)

# Write a function called password_generator() that takes two inputs, first_name and last_name,
#  and then concatenates the last three letters of each and returns them as a string.

first_name = "Reiko"
last_name = "Matsuki"


# this outputs ikouki
def password_generator(first_name, last_name):
    temp_password = first_name[len(first_name) - 3:] + last_name[len(last_name) - 3:]

    return temp_password


temp_password = password_generator(first_name, last_name)

print(temp_password)
