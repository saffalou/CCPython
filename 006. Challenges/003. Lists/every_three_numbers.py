# count every third number
# if start number is >100 return an empty list
def every_three_nums(start):
    return list(range(start, 101, 3))

# start is greater than 100 - return empty list
print(every_three_nums(101))

# start is less than 100 - print number incrementing by 3
print(every_three_nums(90))
