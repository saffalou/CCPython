# single parameter function
# location = parameter
# parameters are treated like variables within a function
# the value/s we pass to the parameters = argument

def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)
# calling the function needs to be outside the function (not indented)
generate_trip_instructions("Central Park")


# 

def generate_new_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)
# calling the function needs to be outside the function (not indented)
generate_new_trip_instructions("Grand Central Station")

