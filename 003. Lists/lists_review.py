#  Name	         Size	    Expedited Shipping
#  "Ainsley"	"Small"	    True
#  "Ben"	    "Large"	    False
#  "Chani"	    "Medium"	True
#  "Depak"	    "Medium"	False
#

# Your code below: 
first_names = ["Ainsley", "Ben", "Chani", "Depak"]

preferred_size = ['Small', "Large", "Medium"]

customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]

preferred_size.append("Medium")

#print(preferred_size)

print(customer_data)

#modify expedited shipping value for Chani
customer_data [2][2] = False

print(customer_data)

#remove expedite shipping detail for Ben
customer_data[1].remove(False)
print(customer_data)

# add more customers to customer data
customer_data_final = customer_data + [["Amit", 'Large', True], ["Karim", "X-Large", False]]

print(customer_data_final)