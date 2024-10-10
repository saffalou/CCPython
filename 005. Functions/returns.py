# Functions can also return a value to the program so that this value can be modified or used later
# We use the Python keyword return to do this
# When there is a result from a function that is stored in a variable, it is called a returned function value
def calculate_exchange_usd(us_dollars, exchange_rate):
  return us_dollars * exchange_rate

new_zealand_exchange = calculate_exchange_usd(100, 1.4)

# we need to stringify the new_zealand_exchange value to concatenate it into the print output
print("100 dollars in US currency would give you " + str(new_zealand_exchange) + " New Zealand dollars")


current_budget = 3500.75
shirt_expense = 9

# create a function that allows us to print out current budget value
def print_remaining_budget(budget):
  print("Your remaining budget, after expenses is: $" + str(budget))

print_remaining_budget(current_budget)

# create a function that enables us to adjust budget remaining based on expenses incurred
# we have 2 parameters and we want to subtract expense from budget
def deduct_expense(budget, expense):
  return budget - expense

# we calculate the remaining budget in this variable by inserting our variables as arguments
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

# we print out the result of the above to see our current_budget remaining value
print_remaining_budget(new_budget_after_shirt)