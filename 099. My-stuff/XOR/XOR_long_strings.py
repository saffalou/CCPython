def xor(phrase, key):
    for char in phrase:
        code = ord(phrase) ^ ord(key)
        output = chr(code)

        return output


phrase = "3"
key = "Z"

encrypted = ""
for letter in phrase:
    encrypted = encrypted + xor(phrase, key)

print(encrypted)
