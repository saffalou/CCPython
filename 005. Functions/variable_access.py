# If a variable lives outside of any function it can be accessed anywhere in the file

# This function will print a hardcoded count of how many locations we have.
def print_count_locations():
  favorite_locations = "Paris, Norway, Iceland"
  print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()

# the above will throw an error because favourite_locations is out of scope
# below we have the same code but it is now correct
# the favourite_locations variable has been moved outside of the function so it is now globally available



favorite_locations = "Paris, Norway, Iceland"

# This function will print a hardcoded count of how many locations we have.
def print_count_locations(): 
  print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()