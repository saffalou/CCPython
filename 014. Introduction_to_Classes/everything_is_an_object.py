# Attributes can be added to user-defined objects after instantiation, so it’s possible for an object to have some attributes that are not explicitly defined in an object’s constructor.
# We can use the dir() function to investigate an object’s attributes at runtime.
# dir() is short for directory and offers an organized presentation of object attributes.

print(dir(5))

print("\n")


def this_function_is_an_object():
    return "Wow"


print(dir(this_function_is_an_object))
print("\n")


fun_list = [10, "string", {'abc': True}]

print(type(fun_list))
print("\n")

print(dir(fun_list))
print("\n")

class Examine:

    class_var = "This is a class variable"

    def __init__(self):
        self.inst_var = "This is an instance variable"


myobj = Examine()

# calling dir() on class
print(dir(Examine))
print("\n")
# OUTPUTS: ['__doc__', '__init__', '__module__', 'class_var']

# calling dir on object
print(dir(myobj))
# OUTPUTS: ['__doc__', '__init__', '__module__', 'class_var', 'inst_var']
