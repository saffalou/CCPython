# calculate the average of 2 numbers

def average(num1, num2):
    return (num1 + num2) / 2


# The average of 1 and 100 is 50.5
print(average(1, 100))

# The average of 1 and -1 is 0
print(average(1, -1))


# alternate approach
def average(num1, num2):
    total = num1 + num2
    count = 2
    return total / count


# The average of 1 and 100 is 50.5
print(average(1, 100))

# The average of 1 and -1 is 0
print(average(1, -1))


# or this way
def average(num1, num2):
    return (num1 + num2) / 2


# The average of 1 and 100 is 50.5
print(average(1, 100))

# The average of 1 and -1 is 0
print(average(1, -1))
