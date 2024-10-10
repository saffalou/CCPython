# In this lesson, we learned how to:

# Add elements to a list by index using the .insert() method.
# Remove elements from a list by index using the .pop() method.
# Generate a list using the range() function.
# Get the length of a list using the len() function.
# Select portions of a list using slicing syntax.
# Count the number of times that an element appears in a list using the .count() method.
# Sort a list of items using either the .sort() method or sorted() function.


inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[0:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory.pop(4)
inventory.insert(10,"19th Century Bed Frame")
inventory_sorted = sorted(inventory)
inventory.sort()

print(f'Inventory length {inventory_len}\n')

print(f'First item {first}\n')

print(f'Last item {last}\n')

print(f'Inventory_2_6 {inventory_2_6}\n')

print(f'First_3 {first_3}\n')

print(f'Twin beds count: {twin_beds}\n')

print(f'Updated inventory: {inventory}\n')

print(f'Sorted inventory: {inventory_sorted}\n')

print(f'Using .sort(): {inventory}\n')



