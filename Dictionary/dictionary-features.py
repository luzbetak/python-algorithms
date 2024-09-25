print("--------------- Filtering ------------------------------")
a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {k: v for k, v in a_dict.items() if v <= 2}
print(new_dict)

print("--------------- Calculation ----------------------------")
incomes = {'Kevin': 5600.00, 'Thomas': 3500.00, 'Luzbetak': 5000.00}
total_income = sum(incomes.values())
print(total_income)

print("--------------- Sorted by Keys -------------------------")
incomes = {'Kevin': 5600.00, 'Thomas': 3500.00, 'Luzbetak': 5000.00}
for key in sorted(incomes):
    print(key, '->', incomes[key])

print("--------------- Sorted by Value -------------------------")
incomes = {'Kevin': 1000.00, 'Thomas': 2000.00, 'Luzbetak': 3000.00}


def by_value(element):
    return element[1]


for k, v in sorted(incomes.items(), key=by_value):
    print(k, '->', v)

print("----------------- Sorted Reverse ------------------------")
incomes = {'Kevin': 5600.00, 'Thomas': 3500.00, 'Luzbetak': 5000.00}
for key in sorted(incomes, reverse=True):
    print(key, '->', incomes[key])

print("--------------- Filter Elements ------------------------")
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}


def has_low_price(price):
    return prices[price] < 0.4


low_price = list(filter(has_low_price, prices.keys()))
print(low_price)

print("--------------- Map All Elements ------------------------")
prices = {'apple': 2.40, 'orange': 3.35, 'banana': 4.25}


def discount(price):
    return price[0], round(price[1] * 0.85, 2)


new_prices = dict(map(discount, prices.items()))
print(new_prices)

print("----------------- Unpacking Operator ** -----------------")
fruit_prices = {'apple': 0.40, 'orange': 0.35}
vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
for k, v in {**vegetable_prices, **fruit_prices}.items():
    print(k, '->', v)
