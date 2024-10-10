# booleans are either True or False
# booleans are not assigned as strings
# the following shows what happens when we check the boolean type as entered in the variable - the type returns as string (str)
my_baby_bool = 'true'

print(type(my_baby_bool))

# now when it is created without the ''. The type returns as boolean (bool)
my_baby_bool_two = True

print(type(my_baby_bool_two))

# If we want to catch Dave or another user trying to log into our computer (swap between user names)

# Enter a user name here, make sure to make it a string
#user_name = 'angela_catlady_87'
#user_name = 'Dave'
user_name = 'Alex'

if user_name == "Dave":
  print("Get off my computer Dave!")

if user_name == 'angela_catlady_87':
  print('I know it is you, Dave! Go away')

if user_name == 'Alex':
    print('Welcome to my computer. Please be nice to it')
