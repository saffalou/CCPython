#  The program below converts decimal numbers to their binary representations.
#  It uses the bin() function, which accepts an integer input (which in this case is the variable num, and returns a string output that is stored in the variable binary).
#  The last line prints out the value of binary
#  (0b indicates that the number is in binary format).

# num = input("Enter number to convert: ")
# num = int(num)
# binary = bin(num)
# print(binary)

# convert a single letter to  binary
text = input("Enter a letter to convert: ")

bin_conv = bin(ord(text))
print(bin_conv)

# convert a string
my_string = input("Add your letter, word or sentence here: ")
string_to_binary = [bin(ord(i)) for i in my_string]

binary_output = ''.join(string_to_binary)
print(binary_output)

#  convert binary to string
n = 8
bin1 = binary_output.replace('b', '')

bin_to_text = [(bin1[i : i+n]) for i in (range(0, len(bin1)), n)]

print(bin_to_text)

# binary_data_split = binary_data.split
# ascii_string = ""
# for binary_segment in binary_data.split(' '):
#      decimal_data = int(binary_segment, 2)
#      ascii_char = chr(decimal_data)
#      ascii_string += ascii_char
# print(ascii_string)  # returns 'hello'
#
# print(binary_data)
# print(new_binary)
