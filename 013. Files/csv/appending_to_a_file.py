# Instead of opening the file using the argument 'w' for write-mode, we open it with 'a'

# start with a  file that contains the following text "What an incredible file!"
# and then append an additional line (note the use of new line)

with open('generated_file.txt', 'a') as gen_file:
    gen_file.write("\n... and it still is")

# Notice that opening the file in append-mode, with 'a' as an argument to open(),
# means that using the file object’s .write() method appends whatever is passed to the end of the file
# and will keep adding the appends for as long as we run them (or we run out of hard drive or memory)

#  append entry to file
# every time we run this file the following will be appended to the target file
with open("cool_dogs.txt", "a") as cool_dogs_file:
    cool_dogs_file.write('Air Buddy, ')

# read the file
with open('cool_dogs.txt') as cool_dogs_out:
    doggy_print = cool_dogs_out.read()

    # print the file
    print(doggy_print)
