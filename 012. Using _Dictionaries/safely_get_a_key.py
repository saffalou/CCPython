# Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using.
# If the key you are trying to .get() does not exist, it will return None by default:

building_heights = {
    "Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599,
    "Lotte World Tower": 554.5, "One World Trade": 541.3
}

# this line will return 632:
building_heights.get("Shanghai Tower")
print(building_heights.get("Shanghai Tower"))

# this line will return None as they key does not exist
building_heights.get("My House")
print(building_heights.get("My House"))


user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)

stack_id = user_ids.get("superStackSmash", 100000)

#  this will print 100019 as the key exists
print(tc_id)

# this will print 100000 as the key does not exist
print(stack_id)
