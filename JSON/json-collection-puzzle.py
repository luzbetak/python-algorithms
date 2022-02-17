# ---------------------------------------------------------------------#
import json
import pprint

# ---------------------------------------------------------------------#
pp = pprint.PrettyPrinter()

list1 = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

print("+" + "-" * 50)
print("List: "),
print("+" + "-" * 50)
print(type(list1))
pp.pprint(list1)


# ---------------------------------------------------------------------#
for item in list1:

    print(type(item))
    print(item)
    print("-" * 50)

    # -------------------------------------------#
    if isinstance(item, dict):
        for key in item:
            print(item[key])

            # -----------------------------------#
            if isinstance(item[key], list):
                for value in item[key]:
                    print(value)

# ---------------------------------------------------------------------#

print("+" + "-" * 50)
print("| Dictionary ")
print("+" + "-" * 50)

d = {'abc': 'abc', 'def': {'ghi': 'ghi', 'jkl': 'jkl'}}
for element in d.values():
    print(element)

    if isinstance(element, dict):
        for k, v in element.items():
            print(k, ' ', v)
