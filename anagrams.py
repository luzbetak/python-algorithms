# -------------------------------------------------- #
# ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# -------------------------------------------------- #

from collections import defaultdict
a_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(a_list)
a_dict = defaultdict(list)

for x in a_list:
    a_dict[str(sorted(x))].append(x)

for key, value in a_dict.items():
    print(key, " -> ", value)

# -------------------------------------------------- #
# ['a', 'e', 't']  ->  ['eat', 'tea', 'ate']
# ['a', 'n', 't']  ->  ['tan', 'nat']
# ['a', 'b', 't']  ->  ['bat']
# -------------------------------------------------- #

