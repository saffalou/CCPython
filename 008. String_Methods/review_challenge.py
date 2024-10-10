highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987 \n"

# print("Printing the list as is, no changes \n", highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",")

# print("Before stripping white space but after splitting\n", highlighted_poems_list)

highlighted_poems_stripped = []
for poems in highlighted_poems_list:
    highlighted_poems_stripped.append(poems.strip())

# print("\nAfter splitting and removing excess whiitespace\n", highlighted_poems_stripped)


highlighted_poems_details = []
for colon in highlighted_poems_stripped:
    highlighted_poems_details.append(colon.split(":"))

# print("\nAfter splitting highlighted_poems_stripped\n", highlighted_poems_details)

#  now we want to split out the content so that each publication is on its own line
titles = []
poets = []
dates = []
publications =[]
for poem_title in highlighted_poems_details:
  titles.append(poem_title[0])
for names in highlighted_poems_details:
  poets.append(names[1])
for years in highlighted_poems_details:
  dates.append(years[2])

for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))

