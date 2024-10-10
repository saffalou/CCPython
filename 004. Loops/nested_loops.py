project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

# the following will print the teams
for team in project_teams:
  print(team)

#  but what if we wanted to print each individual student?

# Loop through each sublist
for team in project_teams:
  # Loop elements in each sublist
  for student in team:
    print(student)


# print inside the loop and we print each scoop sold number and add them to finish at the total
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
    # print(location)
  for element in location:
    scoops_sold += element
    print(scoops_sold)

# move the print to outside the loop and we print only the total of all scoops sold 
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
    # print(location)
  for element in location:
    scoops_sold += element
print("\nTotal ice cream scoops sold:",scoops_sold)