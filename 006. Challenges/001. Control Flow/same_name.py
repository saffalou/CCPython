# your_name = ""
# my_name = ""
# Write your same_name function here:
def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
    return False

# test same_name function:
# should print True
print(same_name("Colby", "Colby"))
# should print False
print(same_name("Tina", "Amber"))
