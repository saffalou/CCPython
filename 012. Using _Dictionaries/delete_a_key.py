# Sometimes we want to get a key and remove it from the dictionary
# We can use .pop() to do this.
# Just like with .get(), we can provide a default value to return if the key does not exist in the dictionary
# .pop() works to delete items from a dictionary, when you know the key value


# In one line:
# add the corresponding value of the key "stamina grains" to the health_points variable
# and remove the item "stamina grains" from the dictionary.
# If the key does not exist, add 0 to health_points.

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

# let's check both items here
print(health_points)
print(available_items)

# now check them here to see that the pop has worked and whether we have applied the default value or the assigned value
# note we only use the default value if the key does not exist
health_points += available_items.pop("stamina grains", 0)
print(health_points)
print(available_items)

# now check them here to see that the pop has worked and whether we have applied the default value or the assigned value
health_points += available_items.pop("power stew", 0)
print(health_points)
print(available_items)

# now check them here to see that the pop has worked and whether we have applied the default value or the assigned value
# default 0 will be added here as "mystic bread" is not a key in the dictionary
health_points += available_items.pop("mystic bread", 0)
print(health_points)
print(available_items)

