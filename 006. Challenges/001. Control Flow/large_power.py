# base = 0
# exponent = 0
# Write your large_power function here:
def large_power(base, exponent):
  if (base ** exponent) >5000:
    return True
  else:
    return False  
# test large_power function:
# should print True
print(large_power(2, 13))
# should print False
print(large_power(2, 12))
