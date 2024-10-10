# Methods can also take more arguments than just self:
class Circle:                                 # class
  pi = 3.14                                    # class variable

  def area(self, radius):                  # method
    return Circle.pi * radius ** 2

pizza_diameter = 12
teaching_table_diameter = 36
round_room_diameter = 11460

#   Notice again that even though .area) takes two arguments in its definition,
#   we only pass radius, because self is implicitly passed (and refers to the object circle.

circle = Circle()                                                                                 # object
pizza_area = circle.area(pizza_diameter/2)
teaching_table_area = circle.area(teaching_table_diameter/2)
round_room_area = circle.area(round_room_diameter/2)


print('A 12 inch diameter pizza has the following area:',pizza_area,'inches')

print('A 36 inch diameter teaching table has the following area:',pizza_area,'inches')

print('An 11,460 inch diameter teaching table has the following area:', round_room_area,'inches')
