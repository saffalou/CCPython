# We can overwrite the value of "oatmeal" like this:

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before change to oatmeal price", menu, '\n')

menu["oatmeal"] = 5
print("After change to oatmeal price", menu)



oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print("Original list", oscar_winners, "\n")

# add supporting actress and winner to dictionary
oscar_winners['Supporting Actress'] = "Viola Davis"
print("Supporting actress added", oscar_winners, "\n")

# amend the best picture winner
oscar_winners["Best Picture"] = "Moonlight"
print("After Best Picture amended", oscar_winners)
