# The below script creates a temporary file object called keats_sonnet that points to the file keats_sonnet.txt.
# It then iterates over each line in the document and prints the entire file out.
with open('keats_sonnet.txt') as keats_sonnet:
    for line in keats_sonnet.readlines():
        print(line)


#  We can use the .readlines() function to read a text file line by line instead of having the whole thing.
#  Suppose we have a file "how_many_lines.txt:

with open('how_many_lines.txt') as lines_doc:

# use a for loop to iterate through each line of text in the file
    for lines in lines_doc.readlines():
        print(lines)

