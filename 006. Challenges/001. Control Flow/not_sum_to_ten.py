# do the numbers sum to 10?
num1 = 6
num2 = 2

if num1 + num2 == 10:
  not_ten = True
else:
  not_ten = False

print("Does the sum of the numbers equal 10? " + str(not_ten))


# or could do it this way
# do the numbers sum to 10?
num1 = 6
num2 = 4

if num1 + num2 != 10:
  not_ten = False
else:
  not_ten = True

print("Does the sum of the numbers equal 10? " + str(not_ten))