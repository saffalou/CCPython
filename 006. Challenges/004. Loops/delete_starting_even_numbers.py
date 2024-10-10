#  The function should remove elements from the front of my_list until the front of the list is not even.
#  The function should then return my_list.

def delete_starting_evens(my_list):
    while len(my_list) > 0 and my_list[0] % 2 == 0:
        my_list = my_list[1:]
    return my_list


# returns only the odd numbers
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))

#  returns an empty list as all numbers are evens
print(delete_starting_evens([4, 8, 10]))
