#  sourced from  https://www.educative.io/answers/xor-encryption-of-plaintext-with-a-key-in-python

# Function to perform XOR encryption
def xor_encryption(text, key):
    # Initialize an empty string for encrypted text
    encrypted_text = ""

    # Iterate over each character in the text
    for i in range(len(text)):
        encrypted_text += chr(ord(text[i]) ^ ord(key[i % len(key)]))

    # Return the encrypted text
    return encrypted_text


# The plaintext that we want to encrypt
plain_text = "a"
# The secret key used for encryption
key = "B"

# Encrypt the plain_text using the key
encrypted_text = xor_encryption(plain_text, key)
# Print the encrypted text
print(f'Encrypted Text: {encrypted_text}')

print(f'unencrypted: {xor_encryption(encrypted_text, key)}')
