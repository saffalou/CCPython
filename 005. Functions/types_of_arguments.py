# POSITIONAL ARGUMENTS
# Their assignments depend on their positions in the function call

# In this function, miles_to_travel is positioned as the first parameter
# rate is positioned as the second parameter
# discount is the third 
def calculate_taxi_price(miles_to_travel, rate, discount):
    print(miles_to_travel * rate - discount )

# When we call our function, the position of the arguments will be mapped to the positions defined in the function declaration.
# 100 is miles_to_travel
# 10 is rate
# 5 is discount
calculate_taxi_price(100, 10, 5)

# keyword arguments
#  we explicitly refer to what each argument is assigned to in the function call
calculate_taxi_price(miles_to_travel=100, rate=0.5, discount=10, )

# default arguments
# We can provide a default value to a parameter by using the assignment operator (=).
# This will happen in the function declaration rather than the function call.
# calculate_taxi_price function will always have a default value of 10 in the following example
def calculate_taxi_price(miles_to_travel, rate, discount = 10):
    print(miles_to_travel * rate - discount )
  
# Using the default value of 10 for discount.
calculate_taxi_price(10, 0.5)

# Overwriting the default value of 10 with 20
calculate_taxi_price(10, 0.5, 20)


# in this example we arre using assigned default for final destination
def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
    print("Here is what your trip will look like!")
    print("First, we will stop in "+first_destination+", then "+second_destination + ", and lastly "+ final_destination+"\n")
  
trip_planner("France", "Germany")

# same example as above but now we are overriding the default value of final_destination
def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
    print("Here is what your trip will look like!")
    print("First, we will stop in "+first_destination+", then "+second_destination + ", and lastly "+ final_destination +"\n")
trip_planner("France", "Germany", "Denmark")

# now we change the position of the arguments which changes the print output
# Write your code below:
def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
    print("Here is what your trip will look like!")
    print("First, we will stop in "+first_destination+", then "+second_destination + ", and lastly "+ final_destination + "\n")
trip_planner("Denmark", "France", "Germany")

# or we can use the keyword arguments
# note that we added them in the wrong order in the function call but becuase we used keyword it prints in desired order
def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
    print("Here is what your trip will look like!")
    print("First, we will stop in "+first_destination+", then "+second_destination + ", and lastly "+ final_destination +"\n")
trip_planner(first_destination = "Iceland", final_destination = "Germany", second_destination = "India")