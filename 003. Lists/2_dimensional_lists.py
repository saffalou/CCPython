#Lists can contain other lists! We will commonly refer to these as two-dimensional (2D) lists

heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]]

ages = [['Aaron', 15],['Dhruti', 16]]


print(heights)

print(ages)
#3 this gives us name and height at index 1
print(heights[1])


# this gives us just the height from index 1
print (heights[1][1])

# or we can create variable to call specific list elements based on index
jenny_height = heights[[0][0]]
alexus_height = heights[[1][0]]
sams_height = heights[[2][0]]
grace_height = heights[[3][0]]
vik_height = heights[[4][0]]

print(jenny_height)
print(alexus_height)
print(sams_height)
print(grace_height)
print(vik_height)

#or I can retrieve just 1 element from the index
sams_height_only = heights[2][1]
print(sams_height_only)


#Your code below: 

#Checkpoint 1
class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)

#Checkpoint 2
sams_score = class_name_test[2][1]
print(sams_score)

#Checkpoint 3   -ve index reference
ellies_score = class_name_test[-1][-1]
print(ellies_score)

#same as above but using -ve and +ve index values
ellies_score = class_name_test[-1][1]
print(ellies_score)