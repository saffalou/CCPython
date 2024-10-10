# The function range() takes a single input, and generates numbers starting at 0 and ending at the number before the input.

# if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9

# The range() function is unique in that it creates a range object. It is not a typical list like the ones we have been working with.

# In order to use this object as a list, we have to first convert it using another built-in function called list().

# The list() function takes in a single input for the object you want to convert.


number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)
# if we print just the range
print(zero_to_seven)

# if we convert the range to a list
print(list(zero_to_seven))

# By default, range() creates a list starting at 0. However, if we call range() with two inputs, we can create a list that starts at a different number.

# For example, range(2, 9) would generate numbers starting at 2 and ending at 8 (just before 9):

# If we use a third input, we can create a list that “skips” numbers.

# For example, range(2, 9, 2) will give us a list where each number is 2 greater than the previous number


# remember that because we index from 0 and end point of 15 is actually 15-1 (or 14) meaning that 15 will not appear as that exceeds our range
range_five_three = range(5, 15, 3)
print(list(range_five_three))

range_diff_five = range(0, 40, 5)
print(list(range_diff_five))

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps",
             "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 10)

# calculate the length of long_list
long_list_len = len(long_list)
print(long_list_len)

# calculate the length of big_range
big_range_length = len(big_range)
print(big_range_length)
