thought_1 = 'time for lunch'
thought_2 = " because I'm hungry"

print(thought_1 + thought_2)

name = 'Peter'
name_2 = 'Penny'

print("I know your name, it's " + name)


#formatted string - f strings
print(f"I know your name, it's {name}")

print(f"Hey everybody, {thought_1} {thought_2}, I know your name, it's {name}")


print(f"I know your name, it's {name_2}\n")  #new line added. this will create space between this print and the next

print(f"Hey everybody, {thought_1} {thought_2}, I know your name, it's {name_2}")

long_print = '''
you can create multiple lines of print by 
setting up with three leading single, or double, quote marks
and closing it with a matching set of three quote marks.
'''
print(long_print)

#turn an int into a string

number_of_people =str(4*20)
number_of_people2 = 100*3

print(f"The number of people who attended the shop is {number_of_people}")

print(f"The number of people who attended the shop is {number_of_people2}")

# coverting int to string to concatenate
print('The number of people who attended the shop today is ' + number_of_people)

# because we are tring to concatenate a string and an int this one will throw and error - TypeError: can only concatenate str (not "int") to str
print('The number of people who attended the shop today is ' + number_of_people2)




