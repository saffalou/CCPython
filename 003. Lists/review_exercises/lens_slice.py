# Your code below:
toppings = ["pepperoni","pineapple" ,"cheese" ,"sausage" ,"olives" ,"anchovies" ,"mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

#how many $2 slices are there?
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
print('\n')        # adds readability when printing to the terminal

# how many different pizzas are there
num_pizzas = len(toppings)
print(num_pizzas)
print("\n")

print(f'We sell {num_pizzas} different kinds of pizza!')
print("\n")

# 2D list of pizza prices and pizza type
pizza_and_prices = [[2, "pepperoni"],[6, "pineapple"],[1, "cheese"],[3, "sausage"],[2, "olives"],[7, "anchovies"],[2, "mushrooms"]]

print(pizza_and_prices)
print("\n")

#the default sort is to sort ascending based on price - observe the first print then the one post sort
pizza_and_prices.sort()

print(pizza_and_prices)
print("\n")

# return the cheapest pizza slice. Because of the sort the cheapest will be first so we want to return first record
cheapest_pizza = pizza_and_prices[:1]
print(cheapest_pizza)
print("\n")         
priciest_pizza = pizza_and_prices[-1:]
print(priciest_pizza)
print("\n")
#because of the pizza_and_prices
anchovies_popped = pizza_and_prices.pop()
print(anchovies_popped)
print("\n")
pizza_and_prices.insert(4, [2.5, "peppers"])
print(f"Latest pizza list and prices:\n{pizza_and_prices}\n")
#or
print("Latest pizza list and prices:\n",pizza_and_prices)

print('\n')

three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)
