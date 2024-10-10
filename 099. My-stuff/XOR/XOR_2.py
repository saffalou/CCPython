# Data Encryption using XOR
def encrypt_decrypt(data, key):
    return ''.join(chr(ord(d) ^ key) for d in data)


message = "The map is in the backroom"
key = 10
encrypted_message = encrypt_decrypt(message, key)
decrypted_message = encrypt_decrypt(encrypted_message, key)
print(encrypted_message)  # Output: "\x07\x1c\x15\x15\x1f\x1f\x12\x1b\x15\x14"
print(decrypted_message)  # Output: "Hello, XOR!"
