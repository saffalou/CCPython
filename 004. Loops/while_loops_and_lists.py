# Similar to how we saw for loops working with lists, we can use while loops to iterate through a list as well.
# while loops require some form of a variable to track the condition of the loop to start and stop.

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

length = len(ingredients)
index = 0

while index < length:
  print(ingredients[index])
  index += 1
  
  
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
index = 0
while index < length:
  print("I am learning about",python_topics[index])
  index +=1
print("\n")  
  
  
  #repeat the above but this time change the increment
length = len(python_topics)
index = 0
while index < length:
  print("I am learning about every second topic because I changed the index increment",python_topics[index])
  index +=2