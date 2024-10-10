# Create a function named in_range() that has three parameters named num, lower, and upper.
# The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.
num = 0
lower = 0
upper = 0
def in_range(num, lower, upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False
in_range(num, lower, upper)

# test your in_range function:
# should print True
print(in_range(10, 10, 10))

# should print False
print(in_range(5, 10, 20))


