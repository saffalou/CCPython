# A dictionary is an unordered set of key: value pairs.
# It provides us with a way to map pieces of data to each other so that we can quickly find values that are associated with one another.

# A dictionary begins and ends with curly braces { and }.
# Each item consists of a key ("avocado toast") and a value (6).
# Each key: value pair is separated by a comma.
# menu = {"avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)

print(num_cameras)

# dictionary of English and Sindarin words
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

print(translations)


#  Dictionaries in Python rely on each key having a hash value, a specific identifier for the key.
#  If the key can change, that hash value would not be reliable.
#  So the keys must always be unchangeable, hashable data types, like numbers or strings.
#  The moment you attempt to use a list or dictionary as key for a dictionary, you will get a type error.

# This will generate an error - TypeError: unhashable type: 'list'
children = {["Johannes", "Rosmarie", "Eleonore"]:" von Trapp" ,  ["Sonny", "Fredo", "Michael"]:"Corleone" }

# This presentation with the list as the value and not as the key will run without error
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"] }
