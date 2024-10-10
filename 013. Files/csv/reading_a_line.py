# .readline(), which will only read a single line at a time
# If the entire document is read line by line in this way subsequent calls to .readline()
# will not throw an error but will start returning an empty string ("")


# This script also creates a file object called sonnet_doc that points to the file millay_sonnet.txt.
# It then reads in the first line using sonnet_doc.readline() and saves that to the variable first_line.
# It then saves the second line (So make the most of this, your little day,) into the variable second_line
# and then prints it out.
with open('millay_sonnet.txt') as sonnet_doc:
    first_line = sonnet_doc.readline()
    second_line = sonnet_doc.readline()

    print(second_line)

# grab all lines
with open("just_the_first.txt") as first_line_doc:
    first_line = first_line_doc.readline()
    second_line = first_line_doc.readline()
    third_line = first_line_doc.readline()
    fourth_line = first_line_doc.readline()
    fifth_line = first_line_doc.readline()
    sixth_line = first_line_doc.readline()   #there is no 6th line. There are only 5 lines. This will return an empty string, not an error

    # print first line
    print(first_line)
    # print third line
    print(third_line)
    # print empty string as there is no line 6
    print(sixth_line)
