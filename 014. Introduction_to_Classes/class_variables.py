class Musician:
    title = "Rockstar"


drummer = Musician()
# prints Rockstar
print(drummer.title)

# Above we defined the class Musician, then instantiated drummer to be an object of type Musician.
# We then printed out the drummer’s .title attribute, which is a class variable that we defined as the string “Rockstar”.
# If we defined another musician, like guitarist = Musician() they would have the same .title attribute.

guitarist = Musician()
print(guitarist.title)


# You are digitizing grades for Jan van Eyck High School and Conservatory.
# At Jan van High, as the students call it, 65 is the minimum passing grade.
# Create a Grade class with a class attribute .minimum_passing equal to 65.
class Grade:
    minimum_passing = 65
