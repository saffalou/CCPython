# .join() is essentially the opposite of .split(), it joins a list of strings together with a given delimiter.
# The syntax of .join() is:
# 'delimiter'.join(list_you_want_to_join)

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel",
                          "on", "stones"]

# set the delimiter, in this case it's a space (this will add a space between each word)
# then add the source of the join data
reapers_line_one = " ".join(reapers_line_one_words)

print(reapers_line_one)

line_1 = ["Who", "said", "that"]
line_2 = ["All", "men", 'are', "created", "equal?"]

# and we can concatenate multiple lists
all_lines = " ".join(line_1 + line_2)

print(all_lines)
