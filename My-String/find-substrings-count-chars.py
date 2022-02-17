import pprint

pp = pprint.PrettyPrinter(indent=2)


# --------------------------------------------------------------------- #
# Output:
# 2
# ---------------------------------------------------------------------
def count_substrings(str1):
    substring = "one"
    count = str1.count(substring)
    print("-" * 50)
    print(str1)
    print("Number of Substrings '{}': {}".format(substring, count))
    print("-" * 50)


# --------------------------------------------------------------------- #
# Output:
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
# None
# --------------------------------------------------------------------- #
def count_characters(str1):
    dict1 = {}
    for i in str1:
        dict1[i] = dict1.get(i, 0) + 1

    pp.pprint(dict1)
    print("-" * 50)
    print("Number of 'e' chars: {}".format(dict1.get('e')))
    print("-" * 50)


# --------------------------------------------------------------------- #
if __name__ == "__main__":
    count_substrings("one two the four one")
    count_characters("Kevin Thomas Luzbetak")
