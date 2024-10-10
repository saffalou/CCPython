#  The function should return the list whose elements sum to the greater number.
#  If the sum of the elements of each list are equal, return lst1.

def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for num1 in lst1:
        sum1 += num1
    for num2 in lst2:
        sum2 += num2
    if sum1 >= sum2:
        return lst1
    else:
        return lst2


print(larger_sum([1, 9, 5], [2, 3, 7]))


#  the above can be slightly re-written to  use sum
def larger_sum_1(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for number in lst1:
        sum1 = sum(lst1)
    for number in lst2:
        sum2 = sum(lst2)
    if sum1 >= sum2:
        return lst1
    else:
        return lst2


print(larger_sum_1([1, 9, 5], [2, 3, 7]))
