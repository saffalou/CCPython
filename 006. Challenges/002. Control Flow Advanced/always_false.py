# There are some situations that you normally want to avoid when programming using conditional statements. 
# One example is a contradiction. This occurs when your condition will always be false no matter what value you pass into it. 
# Write your always_false function here:

num = 5
def always_false(num):
  if num <= num or num >= num:
    return False
  else:
    return True
# test always_false function:
# should print False
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False
print(always_false(num))

# No matter what value we pass into the function, our condition will always be false since it is not logically possible. 
# You normally want to avoid creating conditions like this.