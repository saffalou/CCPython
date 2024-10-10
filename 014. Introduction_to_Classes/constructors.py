# dunder methods, so-named because they have two underscores (double-underscore abbreviated to “dunder”) on either side of them.
#  __init__() method (note the two underscores before and after the word “init”).
#  This method is used to initialize a newly created object. It is called every time the class is instantiated.

# Methods that are used to prepare an object being instantiated are called constructors

# example 1
class Shouter:
    def __init__(self):
        print("HELLO?!\n")


shout1 = Shouter()
# prints "HELLO?!"

shout2 = Shouter()


# prints "HELLO?!"

# example 2
class Shouter:
    def __init__(self, phrase):
        # make sure phrase is a string
        if type(phrase) == str:
            # then shout it out
            print(phrase.upper())


shout1 = Shouter("shout")
# prints "SHOUT"

shout2 = Shouter("shout")
# prints "SHOUT"

shout3 = Shouter("let it all out")


# prints "LET IT ALL OUT"


class Circle:
    def __init__(self, radius):
        self.radius = radius


circle_a = Circle(1)  # instance a
circle_b = Circle(2)  # instance b

print(circle_a.radius)  # 1
print(circle_b.radius)  # 2

from math import pi as PI


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * PI * self.radius


circle_a = Circle(1)
circle_b = Circle(2)

print(circle_a.circumference())  # 6.283185307179586
print(circle_b.circumference())  # 12.566370614359172


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * PI * self.radius

    def area(self):
        return PI * self.radius ** 2


circle_a = Circle(1)
circle_b = Circle(2)

print(circle_a.area())  # 3.141592653589793
print(circle_b.area())  # 12.566370614359172


class Circle:
    pi = 3.14

    # Add constructor here:
    def __init__(self, diameter):
        print('\nNew circle with diameter: {}'.format(diameter))


#  the above prints New circle with diameter: 36

teaching_table = Circle(36)
