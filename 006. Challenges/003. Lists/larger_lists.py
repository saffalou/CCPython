# Let’s say we are working with two conveyor belts that contain items represented by a numerical ID. 
# If one conveyor belt contains more items than the other, then we need to return the ID of the last item on that belt. 
# Define the function to accept two parameters for our two lists of numbers
# Check if the length of the first list is greater than or equal to the length of the second list
# If true, then return the last element from the first list. Otherwise, return the last element from the second list

def larger_list(my_list1, my_list2):
  if len(my_list1) >= len(my_list2):
    return my_list1[-1]
  else:
    return my_list2[-1] 

# note that we are calling the function as part of the print
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))