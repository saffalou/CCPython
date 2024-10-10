# Write a function named remainder() that has two parameters named num1 and num2.
# The function should return the remainder of twice num1 divided by half of num2.
# Multiply the first input value by 2
# Divide the second input value by 2
# Calculate the remainder of the modified first input value divided by the modified second input value (using modulus)
# Return the answer

def remainder(num1, num2):
    double = num1 * 2
    half = num2 / 2
    residual = double % half

    return residual


# should print 2
print(remainder(15, 14))

# should print 0
print(remainder(9, 6))


# a different way to solve the puzzle
def remainder(num1, num2):
    return (2 * num1) % (num2 / 2)


# should print 2
print(remainder(15, 14))

# should print 0
print(remainder(9, 6))
