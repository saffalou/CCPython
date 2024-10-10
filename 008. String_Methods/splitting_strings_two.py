authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

# create a list of authors so that each author is its own string

author_names = authors.split(',')

print(author_names)

# create a list of only the authors first names
author_first_names = []
for first_name in author_first_names:
    author_first_names.append(first_name.split()[0])

print(author_first_names)


# create a list of only the authors last names
author_last_names = []
for name in author_names:
    author_last_names.append(name.split()[-1])

print(author_last_names)



