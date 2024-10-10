#We can use the index -1 to select the last item of a list, 
# even when we don’t know how many elements are in a list.
shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = shopping_list[-1]

index5_element = shopping_list[5]

penultimate_element = shopping_list[-2]
index4_element = shopping_list[4]

print(last_element)

print(index5_element)

print(penultimate_element)

print(index4_element)


if last_element == index5_element:
    print('Same')
    
else:
    print('Different')