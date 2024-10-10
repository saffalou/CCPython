# .format() can be made even more legible for other people reading your code by including keywords.


def favorite_song_statement(song, artist):
    return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)


print(favorite_song_statement("Paranoid", "Black Sabbath"))


# notice that the format order doesn't matter as the keywords are still present
def favorite_song(song, artist):
    return "My favorite song is {song} by {artist}.".format(artist=artist, song=song)


print(favorite_song_statement("Hotel California", "The Eagles"))


def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(
        publishing_date=publishing_date, author=author, title=title,
        original_work=original_work)
    return poem_desc


author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)

print(my_beard_description)
