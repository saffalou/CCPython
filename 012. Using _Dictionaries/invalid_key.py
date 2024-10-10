zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"]
}

key_to_check = "energy"

zodiac_elements["energy"] = "Not a Zodiac element"

# by adding this check we won't get a "KeyError" returned if the key doesn't exist. If the key does exist then the print does its thing
if key_to_check in zodiac_elements:
    print(zodiac_elements["energy"])
