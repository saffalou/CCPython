# When working with strings that come from real data, you will often find that the strings aren’t super clean.
# You’ll find lots of extra whitespace, unnecessary linebreaks, and rogue tabs.
# Stripping a string removes all whitespace characters from the beginning and end
# white space between words is preserved

# You can also use .strip() with a character argument, which will strip that character from either end of the string.


love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ',
                    'you lay down your arms', '           like flowering mines    ',
                    '\n', '   to conquer me home.    ']
#  create a variable to build list of stripped content
love_maybe_lines_stripped = []
# create for loop to loop through the content and strip() the errant spaces
for lines in love_maybe_lines:
    love_maybe_lines_stripped.append(lines.strip())

# use join to reassemble the content and place each sentence on it's own line
love_maybe_full = "\n".join(love_maybe_lines_stripped)

# print the output
print(love_maybe_full)
