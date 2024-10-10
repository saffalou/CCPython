# The .pop() method takes an optional single input:
       # The index for the element you want to remove.

# The method can be called without a specific index. 
# Using .pop() without an index will remove whatever the last element of the list is

# pop() is unique in that it will return the value that was removed. 
# If we wanted to know what element was deleted, simply assign a variable to the call of the .pop() method

# The method can be called with an optional specific index to remove. 
# We don’t have to save the removed value to any variable if we don’t care to use it later.

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 

# we can remove the last item in a list using empty parenthesis
data_science_topics.pop()
print(data_science_topics)

# remove a specific index item - "Algorithms"
data_science_topics.pop(3)
print(data_science_topics)


data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# use pop but add the popped value to a variable keep_it
keep_it = data_science_topics.pop(0)

print(data_science_topics)

print(keep_it)
