# to read a file we can do the following
# with open() where the argument in the method is the file name that we want to read
# we can then save this to a variable

with open('welcome.txt') as text_file:
    text_data = text_file.read()

print(text_data)
