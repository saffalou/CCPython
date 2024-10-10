letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
           "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4,
          10]

# this allows us to score words regardless of whether lower or upper case letters are input
letters += [
    letter.lower()
    for letter
    in letters
]

# this means we allocate same points to lower and upper case for any given letter
points *= 2

# join the 2 lists inside a dictionary so we get letter as key and points as value
letter_to_points = {
    key: value
    for key, value
    in zip(letters, points)
}

print(letter_to_points)

letter_to_points[""] = 0

print(letter_to_points)


def score_word(word):
    points_total = 0
    for letter in word:
        points_total += letter_to_points.get(letter, 0)
    return points_total


# note that the dictionary is in capitals so we need to pass in capitals
# BROWNIES is worth 15 points
word_points = score_word("BROWNIE")
print(word_points)

# but this one is worth only 10 points because the lower case letters don't exist and we set a default value of 0
# in the .get() for lettters that aren't in the dictionary
# note: the code added at line 5 means we now score the entire word
word_points = score_word("BRowNIE")

print(word_points)

# Create a dictionary called player_to_words that maps players to a list of the words they have played
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

print(player_to_words)

# Iterate through the items in player_to_words. Call each player player and each list of words words.
# After the inner loop ends, set the current player value to be a key of player_to_points, with a value of player_points.
# Within your loop, create a variable called player_points and set it to 0.
# After the inner loop ends, set the current player value to be a key of player_to_points, with a value of player_points.
# player_to_points should now contain the mapping of players to how many points they’ve scored.
# wordNerd should win by a point (32 points)
player_to_points = {}


# each new word updates the points total for the player
def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points


update_point_totals()
print(player_to_points)


# this allows players to play a new word and have it added to their played list
def play_word(player, word):
    player_to_words[player].append(word)
    update_point_totals()


play_word("player1", "CODE")

print(player_to_words)
print(player_to_points)






