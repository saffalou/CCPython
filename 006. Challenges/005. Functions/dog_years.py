# Some say that every one year of a human’s life is equivalent to seven years of a dog’s life.
# Write a function named dog_years() that has two parameters named name and age.
# The function should compute the age in dog years and return the following string:
# "{name}, you are {age} years old in dog years"


def dog_years(name, age):
    adjusted_dog_age = age * 7
    output = name + " , you are " + str(adjusted_dog_age) + " years old in dog years"
    return output


# should print "Lola, you are 112 years old in dog years"
print(dog_years("Lola", 16))

# should print "Baby, you are 0 years old in dog years"
print(dog_years("Baby", 0))


# an alternate approach (very similar)
def dog_years(name, age):
    return name + ", you are " + str(age * 7) + " years old in dog years"


# should print "Lola, you are 112 years old in dog years"
print(dog_years("Lola", 16))

# should print "Baby, you are 0 years old in dog years"
print(dog_years("Baby", 0))
