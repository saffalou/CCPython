# while loop and is a form of indefinite iteration.

# A while loop performs a set of instructions as long as a given condition is true.
# The structure follows this pattern:

# while <conditional statement>:
#  <action>


# print the integers 0 through 3:
count = 0
while count <= 3:
  # Loop Body
    print(count)
    count += 1
#  break the loop down:
# count is initially defined with the value of 0. The conditional statement in the while loop is count <= 3, which is true at the initial iteration of the loop, so the loop body executes.
# Inside the loop body, count is printed and then incremented by 1.
# When the first iteration of the loop has finished, Python returns to the top of the loop and checks the conditional again. 
# After the first iteration, count would be equal to 1 so the conditional still evaluates to True and so the loop continues.
# This continues until the count variable becomes 4. At that point, when the conditional is tested it will no longer be True and the loop will stop.

#  Similar to for loops, Python allows us to write elegant one-line while loops. Here is our previous example in a single line:
count = 0
while count <= 3: print(count); count += 1


countdown = 10
#set condition
while countdown >= 0:
  print(countdown)
  # decrement countdown by 1
  countdown -=1
# once we meet our condition we exit the loop and print this statement  
print("We have liftoff!")