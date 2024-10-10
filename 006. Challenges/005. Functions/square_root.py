# Write a function named square_root() that has one parameter named num
#  We then take the one half power of the input value which is mathematically the same as taking the square root and return it.

def square_root(num):
    return num ** (1 / 2)


# should print 4
print(square_root(16))

# should print 10
print(square_root(100))

