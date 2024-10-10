# The def keyword indicates the beginning of a function (also known as a function header). 
# The function header is followed by a name in snake_case format that describes the task the function performs. 
# Following the function name is a pair of parenthesis ( ) that can hold input values known as parameters
# A colon : to mark the end of the function header.
# Lastly, we have one or more valid python statements that make up the function body 

# Your code below: 
# set up the function
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station")
  print("Take the Northbound N, Q, R, or W train 1 stop")
  print("Get off the Times Square 42nd Street stop")

# call the function so that it executes and prints the directions
directions_to_timesSq()




print('Checking the weather for you!')

def weather_check():
  print("Looks great outside! Enjoy your trip.")
  print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")

weather_check()



# compare this to the above. The second print statement in no longer indented within the function 
print('Checking the weather for you!')

def outside_check():
  print("Looks great outside! Enjoy your trip.")
print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")

outside_check()