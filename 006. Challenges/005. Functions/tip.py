#  This function should return the amount you should tip given a total and the percentage you want to tip.
def tip(total, percentage):
    to_be_paid = total * (percentage / 100)
    return to_be_paid


# should print 2.5
print(tip(10, 25))

# should print 0.0
print(tip(0, 100))

# should print 0.0
print(tip(110, 0))

