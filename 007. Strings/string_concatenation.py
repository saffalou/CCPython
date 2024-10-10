# create a new user name from the users
# first 3 letters in first name and last name

first_name = "Julie"
last_name = "Blevins"


def account_generator(first_name, last_name):
    new_account = first_name[0:3] + last_name[0:3]
    return new_account


new_account = account_generator(first_name, last_name)

print(new_account)
