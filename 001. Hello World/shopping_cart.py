#loveseat
lovely_loveseat_description = 'Lovely Loveseat. Tufted polyester blend on wool. 32 inches high x 40 inches wide x 30 inches deep. Red or white \n '
lovely_loveseat_price = 254.00
#settee
stylish_settee_description = 'Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 iinches deep. Black \n'
stylish_settee_price = 180.50
#lamp
luxurious_lamp_description = 'Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.\n'
luxurious_lamp_price = 52.15
#sales tax
sales_tax = 0.088



customer_one_total = 0
customer_one_itemisation = ""
customer_sales_tax = customer_one_total * sales_tax


#customer buys loveseat
customer_one_total = lovely_loveseat_price
customer_one_itemisation = lovely_loveseat_description
#customer buys lamp
customer_one_total += luxurious_lamp_price
customer_one_itemisation += luxurious_lamp_description

total_cost = customer_one_total + customer_sales_tax

print('Customer One Items')
print(customer_one_itemisation)
print('Customer One Total:')
print(total_cost)

