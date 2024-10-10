# python3 datetime reference - https://docs.python.org/3/library/datetime.html
# to use datetime
from datetime import datetime


# to use datetime, as example
# arguments are, year, month, day, hour, minutes, seconds, microseconds, timezone
# the following uses arguments only to seconds

birthday = (1963, 4, 10, 3, 0,)

print(birthday[0])
print(birthday[2])
# datetime.now()  allows us to retrieve the current date and time

print(datetime.now())


# we can use date time to run mathematical operations (only subtraction, cannot use other operators)
# datetime(2018, 1, 1) - datetime(2017, 1, 1)
# the above returns datetime.timedelta(days = 365)

#  or can do the above to work out difference between time now and a past date and time
# datetime.now() - datetime(2018, 1, 1)
#  which returns
#  datetime.timedelta(days=2150, seconds=32554, microseconds=944129)

# strptime - this is way to convert strings into datetime.
#  for example, we might receive a date string "Jan 15, 2018" but we want it in datetime format (2018, 01, 15)
# note that we need to also allow for the spaces
# the arguments are the date string we expect and then the format the string is provided in
# the arguments are specific to required format. Refer https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')

print(parsed_date)

# strftime - allows us to render a date as a string ("f" stands for format)
# we have 2 arguments
            # the date we want to format
            # the format to be used
# the arguments are specific to required format. Refer https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)
