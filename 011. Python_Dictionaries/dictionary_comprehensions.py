# Let’s say we have two lists that we want to combine into a dictionary
# names = ['Jenny', 'Alexus', 'Sam', 'Grace']
# heights = [61, 70, 67, 64]

#  Python allows you to create a dictionary using a dict comprehension, with this syntax:

# students = {key:value for key, value in zip(names, heights)}
# #students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

# Remember that zip() combines two lists into an iterator of tuples with the list elements paired together. This dict comprehension:
# Takes a pair from the iterator of tuples
# Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list)
# Creates a key : value item in the students dictionary
# Repeats steps 1-3 for the entire iterator of pairs


drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

# use zip() to join the lists
zipped_drinks = zip(drinks, caffeine)

# now create the dictionary
drinks_to_caffeine = {key: value for key, value in zip(drinks, caffeine)}

print('\n', drinks_to_caffeine)
