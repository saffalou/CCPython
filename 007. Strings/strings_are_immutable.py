# you cannot change a string in a variable
# strings are immutable
# you can use an existing string to create another string that matches what you need


#  In the following scenario we were given the name "Bob" but the name should be "Rob"
#  if we try something like this  first_name[0] = "R"   it will throw an error
# so we create a new variable and use the part of the string that we can retain and then modify
first_name = "Bob"
last_name = "Daily"

fixed_first_name = "R" + first_name[1:]

print(first_name)

print(fixed_first_name)
