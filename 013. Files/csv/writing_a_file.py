# the .open() function can support 2 arguments
#  argument 1 - the file we want to open to read
# argument 2 - the file we want to write to


# Here we pass the argument 'w' to open() in order to indicate to open the file in write-mode.
# The default argument is 'r' and passing 'r' to open() opens the file in read-mode as we’ve been doing.

# This code creates a new file in the same folder as script.py and gives it the text What an incredible file!.
# It’s important to note that if there is already a file called generated_file.txt it will completely overwrite that file, erasing whatever its contents were before.

with open('generated_file.txt', 'w') as gen_file:
    gen_file.write("What an incredible file!")


# Create a file object for the file bad_bands.txt using the open() function with the w argument.
# Assign this object to the temporary variable bad_bands_doc.
with open("bad_bands.txt", "w") as bad_bands_doc:


# Use the bad_bands_doc.write() method to add the name of a musical group you dislike to the document bad_bands.

    bad_bands_doc.write("Does it get any suckier than Duran Duran!!")
