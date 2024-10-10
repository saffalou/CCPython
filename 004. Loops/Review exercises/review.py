# Create a list called single_digits that consists of the numbers 0-9 (inclusive)
single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []
# Create a for loop that goes through single_digits and prints out each one.
for num in single_digits:
  print(num)
# Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares. 
# You can do this before or after printing the element.
  squares.append(num**2)
print(squares)

# Each element of cubes should be an element of single_digits taken to the third power.
cubes = [num**3 for num in single_digits]
print(cubes)
