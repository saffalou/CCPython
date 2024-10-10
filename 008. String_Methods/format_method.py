#  .format() takes variables as an argument and includes them in the string that it is run on.
#  You include {} marks as placeholders for where those variables will be imported.

def favorite_song_statement(song, artist):
    return "My favorite song is {} by {}.".format(song, artist)


print(favorite_song_statement("Smooth", "Santana"))


# => "My favorite song is Smooth by Santana."


def poem_title_card(title, poet):
    return "The poem {} is written by {}.".format(title, poet)


print(poem_title_card('"I Hear America Singing"', "Walt Whitman"))
