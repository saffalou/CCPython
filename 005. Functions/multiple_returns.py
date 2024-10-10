# Sometimes we may want to return more than one value from a function. 
# We can return several values by separating them with a comma

# create variable and add weather conditions as list
weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']

# create function with single argument
# in function create 3 variables for each day to be reported. 
# Link each to index in weather_data
def threeday_weather_report(weather):
  first_day = " Tomorrow the weather will be " + weather[0]
  second_day = " The following day it will be " + weather[1]
  third_day = " Two days from now it will be " + weather[3]
  return first_day, second_day, third_day

# create 3 variables and link them to our function with the weather_data variable as the argument
tomorrow, following_day, two_days_later = threeday_weather_report(weather_data)

# now print the values for each day
print(tomorrow)
print(following_day)
print(two_days_later)


# create function that contains the 3 most popular destinations
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
# add a return so we can access the functrion variables
  return first, second, third
# create 3 new variables to store the values from the function
most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

# print the variables
print(most_popular1)
print(most_popular2)
print(most_popular3)