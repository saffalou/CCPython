# Create a function named max_num() that takes a list of numbers named nums as a parameter.
# The function should return the largest number in nums

def max_num(nums):
    max_val = nums[0]
    for num in nums:
        max_val = max(nums)
    return max_val


print(max_num([50, -10, 0, 75, 20]))

print(max_num([100, -10, 0, 75, 20]))

print(max_num([100, -10, 0, 100, 20]))


#  an alternate solution
def max_num(nums):
    maximum = nums[0]
    for number in nums:
        if number > maximum:
            maximum = number
    return maximum


print(max_num([50, -10, 0, 75, 20]))

print(max_num([100, -10, 0, 75, 20]))

print(max_num([100, -10, 0, 100, 20]))


# or we can use max() for a more direct solution.
# The task requirement was to not use this option
def max_num(nums):
    large_num = max(nums)
    return large_num


print(max_num([50, -10, 0, 75, 20]))

print(max_num([100, -10, 0, 75, 20]))

print(max_num([100, -10, 0, 100, 20]))
