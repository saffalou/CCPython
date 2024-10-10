# The function should sum the elements of the list until the sum is greater than 9000.
#  When this happens, the function should return the sum.
#  If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements.
#  If the list is empty, the function should return 0.


def over_nine_thousand(lst):
    power_level = 0
    for nums in lst:
        power_level += nums
        #  power_level = sum(lst)
        if power_level > 9000:
            break
    return power_level


#  This return 9020
print(over_nine_thousand([8000, 900, 120, 5000]))

#  This returns only the first element as it exceeds the limit
print(over_nine_thousand([9001, 900, 120, 5000]))

#  This returns 0 as we have an empty list
print(over_nine_thousand([]))


# an alternative solution
def over_nine_thousand(lst):
    total = 0
    for number in lst:
        total += number
        if total > 9000:
            break
    return total
