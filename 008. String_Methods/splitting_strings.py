# .split() is performed on a string, takes one argument, and returns a list of substrings found between the given argument (which in the case of .split() is known as the delimiter).
# The following syntax should be used:
# string_name.split(delimiter)

#  If you do not provide an argument for .split() it will default to splitting at spaces.

#  Important to note: if we run .split() on a string with no spaces, we will get a single element array containing the same string.
#  output will be comma delimited

line_one = "The sky has given over"

line_one_words = line_one.split()

print(line_one_words)

line_two = "Harry, and, Hermoine, and, Ron, went off, on, an, adventure"

line_two_split = line_two.split(",")

print(line_two_split)


line_three = "Break at the #mark"
line_three_split = line_three.split("#")

print(line_three_split)


line_four = "Break at the #mark"
line_four_split = line_four.split("a")

print(line_four_split)


line_five = "Break at the #mark"
line_five_split = line_five.split("")      # this one throws an empty delimiter error

print(line_five_split)
