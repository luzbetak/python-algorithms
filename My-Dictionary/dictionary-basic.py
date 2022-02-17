# -------------------------------------------------------------"
# Python dictionary
# -------------------------------------------------------------"
a_dict = {'one': '1', 'two': '2', 'three': '3'}

print("-------------- Iterate Items ---------------------------")
for key, value in a_dict.items():
    print(key, '->', value)

print("-------------- Iterate Items Return Tuple --------------")
for item in a_dict.items():
    print(item)

print("-------------- Iterate Simple --------------------------")
for key in a_dict:
    print(key + " -> " + a_dict[key])

print("-------------- Iterate Keys ----------------------------")
for key in a_dict.keys():
    print(key, '->', a_dict[key])

print("-------------- Iterate Values --------------------------")
for value in a_dict.values():
    print(value)

print("--------------- Delete Item ----------------------------")
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for key in list(prices.keys()):  # Use a list instead of a view
    if key == 'orange':
        del prices[key]
print(prices)
