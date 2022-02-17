#!/usr/bin/python
import json
import pprint
pp = pprint.PrettyPrinter(indent=2)

# -------------------------------------------------#
my_dict = {
    1: "Los Angeles",
    2: "Agoura Hills",
    3: "Calabasas",
    4: "Malibu",
    5: "Santa Monica"
}

# -------------------------------------------------#
#           Write to JSON
# -------------------------------------------------#
print("--- Write Dictionary to JSON ---")
pp.pprint(my_dict)

with open('cities.json', 'w') as file:
    json.dump(my_dict, file)

# -------------------------------------------------#
#           Read from JSON
# -------------------------------------------------#
print("\n--- Read Dictionary from JSON ---")
new_dict = {}
with open('cities.json') as file:
    new_dict = json.load(file)

pp.pprint(new_dict)
# -------------------------------------------------#
