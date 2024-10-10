# Often we won’t be iterating through a specific list (or any collection), but rather only want to perform a certain action multiple times.
# To create arbitrary collections of any length, we can pair our for loops with the trusty Python built-in function range().

for temp in range(6):
  print("Learning Loops!")
  
# note we are not using temp anywhere inside of the loop body. 
# If we are curious about which loop iteration (step) we are on, we can use temp to track it.
# Since our range starts at 0, we will add + 1 to our temp to represent how many iterations (steps) our loop takes more accurately.

for temp in range(6):
  print("Loop is on iteration number " + str(temp + 1))
  
for temp in range(6):
  print("Learning Loops! " +str(temp+1))  
  
  
promise = "I will finish the python loops module!"

for temp in range(5):
  print(promise)  