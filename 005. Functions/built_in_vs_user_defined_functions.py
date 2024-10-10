# print() and len() are examples of built in functions

destination_name = "Venkatanarasimharajuvaripeta"

# Built-in function: len()
length_of_destination = len(destination_name)

# Built-in function: print()
print(length_of_destination)


tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# using max()
max_price =max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)

# using min()
min_price =min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)

# using round. Note that an argument in round() is the number of decimal places
# compare the following
# note that not adding the second argument produces an int but adding it (even 0) produces a float
rounded_price = round(tshirt_price)
print(rounded_price)

rounded_price = round(tshirt_price,0)
print(rounded_price)

rounded_price = round(tshirt_price,1)
print(rounded_price)

rounded_price = round(tshirt_price,2)
print(rounded_price)