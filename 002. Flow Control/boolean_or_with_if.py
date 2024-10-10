# The boolean operator or combines two expressions into a larger expression that is True if either component is True.
# In English, or implies that if one component is True, then the other component must be False. 
# This is not true in Python. If an or statement has two True components, it is also True.

# Examples of the "or" logic
# True or (3 + 4 == 7)    # True
# (1 - 1 == 0) or False   # True
# (2 < 0) or True         # True
# (3 == 8) or (3 > 4)     # False

credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
  print('You have met at least one of the requirements')