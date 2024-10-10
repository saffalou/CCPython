#  If there are an odd number of elements in my_list, the function should return the middle element.
#  If there are an even number of elements, the function should return the average of the middle two elements.

def middle_element(my_list):
    if len(my_list) % 2 == 0:
        sum_of = my_list[int(len(my_list) / 2)] + my_list[int(len(my_list) / 2) - 1]
        return sum_of / 2
    else:
        return my_list[int(len(my_list) / 2)]


#  with an even number of elements we add the middle 2 and divide by 2
print(middle_element([5, 2, -10, -4, 4, 5]))

#  with an odd number of elements we return only the middle element
print(middle_element([5, 2, 99,  4, 5]))
