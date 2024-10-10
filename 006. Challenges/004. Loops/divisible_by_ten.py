#  Return the count of how many numbers in the list are divisible by 10

def divisible_by_ten(nums):
    counter = 0
    for number in nums:
        if number % 10 == 0:
            counter += 1
    return counter


# this returns 3
print(divisible_by_ten([20, 25, 30, 35, 40]))
