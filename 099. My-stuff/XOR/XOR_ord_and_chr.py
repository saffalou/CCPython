#  When we want to XOR two characters together, first they need to be converted into numbers (so they can be converted into binary).
#  This is done with the ord function.
# To print the resulting character, we can then use the chr function:

a = ord('a')
b = ord('B')
xor = a ^ b
c = chr(xor)
print(c)

char_a = "a"
key = "B"
# ord() returns the number representing the unicode code of a specified character
message = ord(char_a)
cipher_key = ord(key)

xor = message ^ cipher_key

# chr() returns a string representing a character and a Unicode integer
c = chr(xor)

print(c)
