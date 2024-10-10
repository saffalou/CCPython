# Write a function called letter_check that takes two inputs, word and letter.
# This function should return True if the word contains the letter and False if it does not.

def letter_check(word, letter):
    for char in word:
        if char == letter:
            return True
    else:
        return False


print(letter_check("lifelong", "z"))

print(letter_check("alphabet", "l"))
