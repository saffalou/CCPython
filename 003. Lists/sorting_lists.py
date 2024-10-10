
# OPTION 1 - .sort
# We can sort a list using the method .sort()
# standard alpha sort (ascending)
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names.sort()
print(names)

# reverse alpha (descending)
names.sort(reverse=True)
print(names)

# The .sort() method does not return any value and thus does not need to be assigned to a variable since it modifies the list directly. 
# If we do assign the result of the method, it would assign the value of None to the variable. Can see this in below example

cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
# sorted_cities = cities.sort()       #remarked out this line as the linter shows it as an error. Unremark to execute the print
# print(f'When I assign .sort() to a variable it outputs None, just like this example-  {sorted_cities}')


addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)


names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()
print(names)



cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
cities.sort(reverse=True)
print(cities)

# OPTION 2 sorted()
# The sorted() function is different from the .sort() method in two ways:

# It comes before a list, instead of after as all built-in functions do.
# It generates a new list rather than modifying the one that already exists.

# using sorted does not change the list

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
games_sorted = sorted(games)

# sorted list
print(games_sorted)

#unsorted list
print(games)

# the sorted() function will return a list so you must assign the returned data to a new variable
# the sort() function modifies the list in-place and has no return value