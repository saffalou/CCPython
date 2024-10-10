# Dictionaries have a .values() method that returns a dict_values object (just like a dict_keys object but for values!) with all of the values in the dictionary.
# t can be used in the place of a list for iteration:


test_scores = {
    "Grace": [80, 72, 90], "Jeffrey": [88, 68, 81], "Sylvia": [80, 82, 84],
    "Pedro": [98, 96, 95], "Martin": [78, 80, 78], "Dina": [64, 60, 75]
}

#  Will yield the following
# [80, 72, 90]
# [88, 68, 81]
# [80, 82, 84]
# [98, 96, 95]
# [78, 80, 78]
# [64, 60, 75]
for score_list in test_scores.values():
    print(score_list)

#  There is no built-in function to get all of the values as a list, but if you really want to, you can use:
print("\n", list(test_scores.values()))

num_exercises = {
    "functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19,
    "classes": 18, "dictionaries": 18
}

total_exercises = 0

for nums in num_exercises.values():
    total_exercises += nums

print(total_exercises)
