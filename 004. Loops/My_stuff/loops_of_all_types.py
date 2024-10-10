# while loops
target = 10

while target < 20:
    target += 1
    print(target)
print('\n')
    
    
    
start = 1
end = 12
    
while start < end:
        start += 1
        print(start)
print("\n")
        

start = 1
end = 12
  
while end > start:
    end -= 1
    print(end)
print("\n")

# if the print is below the decrement, the first countdown number printed is 9
# if the print is moved above the decrement the countdown starts at 10

countdown_start = 10
lift_off = 0

while countdown_start > lift_off:
    print(countdown_start)
    countdown_start -= 1
    # print(countdown_start)
print("Liftoff. We have liftoff!")

# while loops and lists
freshwater_fish = ["brown trout", "rainbow trout", "english perch", "carp", "tench"]
index = 0
length = len(freshwater_fish)

while index < length:
    print(freshwater_fish[index])
    index +=1
    
colours = ["red", "blue", "yellow", "green", "purple", "orange"]    
colours_length = len(colours)
primary_index = 0

while primary_index < colours_length and primary_index < 3:
    print("This is a primary colour:",colours[primary_index])
    primary_index +=1



# for loops



# for loops using range()


# nested loops



# loop control using breaks




# loop control using continue



# list comprehensions



# list comprehensions using conditionals





