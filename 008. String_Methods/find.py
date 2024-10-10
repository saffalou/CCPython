# .find() takes a string as an argument and searching the string it was run on for that string.
# It then returns the first index value where that string is located.

print('smooth'.find('t'))
# => '4'


print("smooth".find('oo'))
# => '2' (the first occurrence of "o")


god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")        # index where we find the word disown. 20 is the index of the "d" in "disown"

print(disown_placement)
