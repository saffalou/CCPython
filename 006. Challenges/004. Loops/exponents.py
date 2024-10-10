#  Create a function named exponents() that takes two lists as parameters named bases and powers.
#  Return a new list containing every number in bases raised to every number in powers.
def exponents(bases, powers):
    raised = []
    for nums in bases:
        for vals in powers:
            raised.append(nums ** vals)
    return raised


print(exponents([2, 3, 4], [1, 2, 3]))
