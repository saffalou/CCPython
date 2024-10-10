last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

print(gradebook)

# add subject and grade
gradebook.append(["compter science", 100])

print(gradebook)

# add subject and grade
gradebook.append(["visual arts", 93])

print(gradebook)

#amend history grade to be 5 marks higher
gradebook[-1][-1] = 98

print(gradebook)

# remove the grade from poetry
gradebook[2].remove(85)

print(gradebook)

#add grade to poetry but as "pass"
gradebook[2].append("Pass")

print(gradebook)

#use concatentaion to pull both sets of marks together into a single list
full_gradebook = last_semester_gradebook + gradebook
print("These are my grades for the full year\n", full_gradebook)