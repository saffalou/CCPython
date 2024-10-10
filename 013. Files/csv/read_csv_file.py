# In Python we can convert that data into a dictionary using the csv library’s DictReader object

# we first import our csv library, which gives us the tools to parse our CSV file
import csv

# We then create the empty list list_of_email_addresses which we’ll later populate with the email addresses from our CSV
list_of_email_addresses = []
# Then we open the users.csv file with the temporary variable users_csv.
# We pass the additional keyword argument newline='' to the file opening open() function so that
# we don’t accidentally mistake a line break in one of our data fields as a new row in our CSV
with open('users.csv', newline='') as users_csv:
    # After opening our new CSV file we use csv.DictReader(users_csv) which converts
    # the lines of our CSV file to Python dictionaries which we can use access methods for
    # The keys of the dictionary are, by default, the entries in the first line of our CSV file.
    # Since our CSV’s first line calls the third field in our CSV “Email“, we can use that as the key in each row of our DictReader.
    user_reader = csv.DictReader(users_csv)
    for row in user_reader:
        # By accessing the 'Email' key of each of these rows we can grab the email address in that row and append it to our list_of_email_addresses.
        list_of_email_addresses.append(row['Email'])

print(list_of_email_addresses)

