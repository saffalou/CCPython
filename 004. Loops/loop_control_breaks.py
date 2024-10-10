items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

for item in items_on_sale:
  if item == "knit dress":
    print("Found it")
    
# the above code finmds the match - awesome
# but it will check all items in the list before exiting
# you can stop iteration from inside the loop by using break loop control statement.
# When the program hits a break statement it immediately terminates a loop.

items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

print("Checking the sale list!")

for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break

print("End of search!")



dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)

  if dog_breed==dog_breed_I_want:
    print("They have the dog I want!")
    break