# LOOPS
# In programming, this process of using an initialization, repetitions, and an ending condition is called a loop. In a loop, we perform a process of iteration (repeating tasks).

# Programming languages like Python implement two types of iteration:

# - Indefinite iteration, where the number of times the loop is executed depends on how many times a condition is met.

# - Definite iteration, where the number of times the loop will be executed is defined in advance (usually based on the collection size).


# for loop, a type of definite iteration
# In a for loop, we will know in advance how many times the loop will need to iterate because we will be working on a collection with a predefined length

# the general structure of a for loop
    # for <temporary variable> in <collection>:
       # <action>
       
# a break down each of these components:

# A for keyword indicates the start of a for loop.
# A <temporary variable> that is used to represent the value of the element in the collection the loop is currently on.
# An in keyword separates the temporary variable from the collection used for iteration.
# A <collection> to loop over. In our examples, we will be using a list.
# An <action> to do anything on each iteration of the loop.

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

for ingredient in ingredients:
  print(ingredient, "\n")
  
  # ingredient is the <temporary variable>.
# ingredients is our <collection>
# print(ingredient) was the <action> performed on every iteration using the temporary variable of ingredient

# for loops can be written in a single line in python (not recommended for anything beyond simple loops)
for ingredient in ingredients: print(ingredient, "\n")


board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)

for sports in sport_games:
  print(sports)
print("\n")
  
  #  note in this instance the print inside the for loop let's us see the list being built incrementally
  #  the same print outside of the loop just show the final list
  
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_B.append(student)
  # print(student)

  print("Print inside the loop and we can see the list build incrementally",students_period_B)

print("\n")
print("Print outside the loop and we get just the final list of names ",students_period_B)