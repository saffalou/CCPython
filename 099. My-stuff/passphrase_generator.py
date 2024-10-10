import random

passphrase_element_one = ["           ", "Elephant", "Giraffe", "Penguin", "Lion", "Cheetah", "Tiger",
                          "Fish", "Pig", "Squirrel", "Muffin", "Doughnut", "MaGiC",
                          "wATer", "007", "100.00", "Ralph", "Bond-007", "Rock", "Roll",
                          "Quick", "Brown", "Fox", "Lazy", "Dog", "Cat"]
passphrase_element_two = ["is", "at", "miser", "rich", "poor", "@   ", "&&%", "wallet", "Fishing",
                          "GaRLic", "braids", "smarter than", "5.6.7.8.9", "has refuge with ", "an",
                          "wants a", "needs a", "            "]
passphrase_element_three = ["person", "animal", "favourite", "ice cream",
                            "hyphenated-word", "Reason", "Idea", "INCREDIBLE", "1234@5", "           "]


counter = 0

SEPARATOR = " "

while counter < 5:
    counter += 1
    ppe_one_rand = random.choice(passphrase_element_one)
    ppe_two_rand = random.choice(passphrase_element_two)
    ppe_three_rand = random.choice(passphrase_element_three)

    print(ppe_one_rand  + ppe_two_rand + ppe_three_rand)
