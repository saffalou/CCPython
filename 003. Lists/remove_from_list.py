# Your code below: 
order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]

print(order_list)

order_list.remove('Flatbread')

print(order_list)

print(new_store_order_list)

new_store_order_list.remove('Mango')

print(new_store_order_list)

#the following is not part of the list so throws an error "ValueError: list.remove(x): x not in list"
new_store_order_list.remove('Onion')

print(new_store_order_list)