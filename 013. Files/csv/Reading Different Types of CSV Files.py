# we call all files with a list of different values a CSV file and then use different delimiters
# (like a comma or tab) to indicate where the different values start and stop.
'''
Name;Address;Telephone
Donna Smith;126 Orr Corner Suite 857\nEast Michael, LA 54411;906-918-6560
Aaron Osborn;6965 Miller Station Suite 485\nNorth Michelle, KS 64364;815.039.3661x42816
Jennifer Barnett;8749 Alicia Vista Apt. 288\nLake Victoriaberg, TN 51094;397-796-4842x451
Joshua Bryan;20116 Stephanie Stravenue\nWhitneytown, IA 87358;(380)074-6173
Andrea Jones;558 Melissa Keys Apt. 588\nNorth Teresahaven, WA 63411;+57(8)7795396386
Victor Williams;725 Gloria Views Suite 628\nEast Scott, IN 38095;768.708.3411x954
'''
# Notice the \n character, this is the escape sequence for a new line.
# The possibility of a new line escaped by a \n character in our data is why we pass the newline='' keyword argument to the open() function

import csv

with open('addresses.csv', newline='') as addresses_csv:
    address_reader = csv.DictReader(addresses_csv, delimiter=';')
    for row in address_reader:
        print(row['Address'])

with open('books.csv') as books_csv:
    books_reader = csv.DictReader(books_csv, delimiter='@')
    isbn_list = [book['ISBN'] for book in books_reader]

    print("\n")

    print(isbn_list)
