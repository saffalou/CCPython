#  this function identifies whether item1 or item2 appears more
def more_frequent_item(my_list, item1, item2):
    if my_list.count(item1) >= my_list.count(item2):
        return item1
    else:
        return item2


#  in this input item2 appears more
#  it outputs 3 (item 2)
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


#  it outputs 2 as item2 appears only once
print(more_frequent_item([2, 1, 1, 2, 1, 2, 1, 2, 3], 2, 3))

#  it outputs 2 as item2 and item 1 appear same number of times
print(more_frequent_item([2, 3, 3, 2, 3, 2, 1, 2, 3], 2, 3))
