#  Create a function named odd_indices() that has one parameter named my_list.
# The function should create a new empty list and add every element from my_list that has an odd index.
# The function should then return this new list.


def odd_indices(my_list):
    new_list = []
    for index in range(1, len(my_list), 2):                              #  use len(my_list) to set end point of range
        new_list.append(my_list[index])                                 # append the index values to new list
    return new_list


print(odd_indices([4, 3, 7, 10, 11, -2]))
