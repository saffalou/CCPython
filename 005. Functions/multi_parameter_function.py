# Write your code below: 
# We can write a function that takes in more than one parameter by using commas:
# When we call our function, we will need to provide arguments for each of the parameters we assigned in our function definition.
# The ordering of your parameters is important as their position will map to the position of the arguments and will determine their assigned value in the function body

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = (hotel_rate * trip_time) - 10
  print(car_rental_total, hotel_total, plane_ticket_price)


calculate_expenses(200, 100, 100, 5)