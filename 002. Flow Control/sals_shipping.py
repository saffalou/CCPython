weight_lbs = 1.5

# ground shipping
ground_flat_charge = 20.00
premium_ground_shipping = 125.00


if weight_lbs <= 2.0:
  price = weight_lbs * 1.50
elif weight_lbs > 2 and weight_lbs <= 6:
  price = weight_lbs * 3.00
elif weight_lbs > 6 and weight_lbs <= 10:
  price = weight_lbs * 4.00
else:
  price = weight_lbs * 4.75    

total_price = price + ground_flat_charge
 

  #drone shipping

if weight_lbs <= 2.0:
  drone_price = weight_lbs * 4.50
elif weight_lbs > 2 and weight_lbs <= 6:
  drone_price = weight_lbs * 9.00
elif weight_lbs > 6 and weight_lbs <= 10:
  drone_price = weight_lbs * 12.00
else:
  drone_price = weight_lbs * 14.25    

print(f' Ground shipping: {price} + {ground_flat_charge} = ${total_price}')
print(f'Premium ground shipping: {premium_ground_shipping}') 
print(f'Drone shipping cost: ${drone_price}')