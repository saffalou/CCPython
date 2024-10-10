#The Python list method .insert() allows us to add an element to a specific index in a list.

# The .insert() method takes in two inputs:
#    The index you want to insert into.
#    The element you want to insert at the specified index.
#The .insert() method will handle shifting over elements and can be used with negative indices.

front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print("Original list\n", front_display_list)

# Your code below:
#add pineapple to the front of the list
front_display_list.insert(0, "Pineapple")
print("Amended list\n", front_display_list)
