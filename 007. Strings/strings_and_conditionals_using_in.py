# There’s an even easier way than iterating through the entire string to determine if a character is in a string.
#  We can do this type of check more efficiently using "in".
#  "in" checks if one string is part of another string.

# => True
print("e" in "blueberry")

# => False
print("a" in "blueberry")

# it not only works with letters, but with entire strings as well.

# => True
print("blue" in "blueberry")

# => False
print("blue" in "strawberry")

#  It can be helpful to include more than one boolean expression in the same line of code.
#  To do this, use and or and not in between the boolean expressions.

# => False
print("e" in "blueberry" and "e" in "carrot")

# => True
print("e" in "blueberry" and not "e" in "carrot")


# create a function that checks if a string is part of a larger string
def contains(big_string, little_string):
    if little_string in big_string:
        return True
    else:
        return False


print(contains("watermelon", "melon"))

print(contains("watermelon", "berry"))


# create a function that compares 2 words and then returns letters that are common to both
def common_letters(string_one, string_two):
    common = []
    for letter in string_one:
        if (letter in string_two) and not (letter in common):
            common.append(letter)

    return common


print(common_letters("hammer", "bullett"))
