#  Because strings are lists, that means we can iterate through a string using for or while loops.
#  This opens up a whole range of possibilities of ways we can manipulate and analyze strings.

def print_each_letter(word):
    for letter in word:
        print(letter)


favorite_color = "blue"
print_each_letter(favorite_color)


def get_length(test):
    counter = 0
    for letter in test:
        counter += 1
    return counter


print("Add your word and the let the program calculate the number of characters. Character count is: ",get_length("superstitious"))
