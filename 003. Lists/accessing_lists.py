#We can select a single element from a list by using square brackets ([]) and the index of the list item. 
# If we wanted to select the third element from the list, we’d use calls[2]


# Note: When accessing elements of a list, you must use an int as the index. 
# If you use a float, you will get an error. This can be especially tricky when using division. 
# For example print(calls[4/2]) will result in an error, because 4/2 gets evaluated to the float 2.0.

#To solve this problem, you can force the result of your division to be an int by using the int() function. 
# int() takes a number and cuts off the decimal point. For example, int(5.9) and int(5.0) will both become 5. 
# Therefore, calls[int(4/2)] will result in the same value as calls[2], whereas calls[4/2] will result in an error.

employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]

employee_four = employees[3]

print(employees[5])

print(employee_four)

# this one produces an error (IndexError: list index out of range) as the index value is greater than the list of items
print(employees[7])