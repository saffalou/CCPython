# Sometimes we want to operate on all of the keys in a dictionary

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

#  we can use the .list() function to create a list of students in the class
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

print(list(test_scores))

# Dictionaries also have a .keys() method that returns a dict_keys object
# A dict_keys object is a view object
# The dict_keys object returned by .keys() is a set of the keys in the dictionary
# You cannot add or remove elements from a dict_keys object, but it can be used in the place of a list for iteration:

# this retrieves the same data but we return it a line at a time
for student in test_scores.keys():
    print(student)


user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

#  assign all the keys from user_ids to variable
users = user_ids.keys()

#  assign all the keys from num_exercises to variable
lessons = num_exercises.keys()

# print both variables - these will print as a list of dict_keys
print(users, "\n")
print(lessons, "\n")

# extract keys using for loop (same data as above but output is by line and not a list of dict_keys)
for user in user_ids.keys():
    print(user)

# extract keys using for loop (same data as above but output is by line and not a list of dict_keys)
for lesson in num_exercises.keys():
    print(lesson)
