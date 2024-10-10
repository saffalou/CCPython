# in Python we add the not operator to the very beginning of the statement
# This operator is straightforward: when applied to any boolean expression it reverses the boolean value. 
# So if we have a True statement and apply a not operator we get a False statement.

credits = 120
gpa = 1.8

if not credits >= 120:
  print('You do not have enough credits to graduate.')

if not gpa >= 2.0:
  print('Your GPA is not high enough to graduate.')  

if not credits >= 120 and not gpa >= 2.0:
  print('You do not meet either requirement to graduate!')   