import random

first_name = ["John","William","James","Charles","George","Frank","Joseph","Thomas","Henry","Robert","Edward","Harry","Walter","Arthur","Fred","Albert","Samuel","David","Louis","Joe","Charlie","Clarence","Richard","Andrew","Daniel"]
last_name = ["smith","johnson","williams","brown","jones","miller","davis","garcia","rodriguez","wilson","martinez","anderson","taylor","thomas","hernandez","moore","martin","jackson","thompson","white","lopez","lee","gonzalez","harris"]
provider = ["gmail", "amazon", "msoft", "disney","rambler", "charter", "123india", "linternetdrive", "abbeyroadlondon"]
dot = ["com", "org", "msn", "cdk", "net", "am", "ru", "au", "uk"]

counter = 0

SEPARATOR = "_"
DOMAIN = "@"
DOT = "."

while counter <5:
    counter += 1
    fn_rand = random.choice(first_name).lower()
    ln_rand = random.choice(last_name)
    prov_rand = random.choice(provider)
    type_rand = random.choice(dot)
    print(fn_rand + SEPARATOR + ln_rand + DOMAIN + prov_rand + DOT + type_rand)
