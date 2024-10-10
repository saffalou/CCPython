# this function  slices the provided list
def remove_middle(my_list, start, end):
    return my_list[:start] + my_list[end + 1:]


# we will print out the list with  index positions 1, 2 and 3 removed
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


# we will print out the list with  index positions 3, 4, 5, 6 and 7 removed
print(remove_middle([4, 8, 15, 16, 23, 42, 22, 99.,5], 3, 7))
