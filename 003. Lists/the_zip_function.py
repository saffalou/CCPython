# In Python, we have an assortment of built-in functions that allow us to build our programs faster and cleaner. 
# One of those functions is zip().
# The zip() function allows us to quickly combine associated data-sets without needing to rely on multi-dimensional lists. 

names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]

names_and_heights = zip(names, heights)

# the print output will be the location of the of the variable in our computers memory
print(names_and_heights)

# we can covert this by using the list() function

converted_list = list(names_and_heights)

#now we can print the list and names and heights
print(converted_list)

# note the output of print(converted_list).
# Our data set has been converted from a zip memory object to an actual list (denoted by [ ])
# Our inner lists don’t use square brackets [ ] around the values. 
# This is because they have been converted into tuples (an immutable type of list)

owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

#Use zip() to create a new variable called names_and_dogs_names that combines owners and dogs_names lists into a zip object.
names_and_dogs_names = zip(owners, dogs_names)

# Then, create a new variable named list_of_names_and_dogs_names by calling the list() function on names_and_dogs_names.
list_of_names_and_dogs_names = list(names_and_dogs_names)

# Print list_of_names_and_dogs_names.
print(list_of_names_and_dogs_names)