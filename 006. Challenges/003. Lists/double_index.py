# The function should return a new list where all elements are the same as in my_list except for the element at index.
#  The element at index should be double the value of the element at index of the original my_list.
#  If index is not a valid index, the function should return the original list.
def double_index(my_list, index):
    # Checks to see if index is too big
    if index >= len(my_list):
        return my_list
    else:
        # Gets the original list up to index
        my_new_list = my_list[0:index]
        # Adds double the value at index to the new list
        my_new_list.append(my_list[index] * 2)
        #  Adds the rest of the original list
        my_new_list = my_new_list + my_list[index + 1:]
    return my_new_list


# Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
