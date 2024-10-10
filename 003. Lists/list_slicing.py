# In Python, often we want to extract only a portion of a list. Dividing a list in such a manner is referred to as slicing.

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# select the full suitace list
beginning = suitcase[0:5]

#select only the middle slice - remember we go to 1 less than the end index value
middle = suitcase[2:4]

#select the final 2 items - remember we go to 1 less than the end index value
end_slice = suitcase[4:6]


print(beginning)

print(middle)

print(end_slice)


# we can slice in different ways
# we can slice just the first element of the list
first_item = suitcase[:1]
print(first_item)

# print only the third item
third_item_in_suitcase = suitcase[4]
print(third_item_in_suitcase)

#print up to and including the third item
many_items = suitcase[:4]
print(many_items)

# print only last 2 elements
last_two_elements = suitcase[-2:]

print(last_two_elements)

# print last 3 elements
slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)