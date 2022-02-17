# ----------------------------------------------------------- #
# ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# ----------------------------------------------------------- #
from collections import defaultdict


# ----------------------------------------------------------- #
def group_by_anagram(list1):
    a_dict = defaultdict(list)
    for x in list1:
        a_dict[str(sorted(x))].append(x)

    return a_dict


# ----------------------------------------------------------- #
if __name__ == "__main__":

    a_list = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    result = group_by_anagram(a_list)
    for key, value in result.items():
        print("{} -> {}".format(key, value))

# ----------------------------------------------------------- #
# ['a', 'e', 't'] -> ['eat', 'tea', 'ate']
# ['a', 'n', 't'] -> ['tan', 'nat']
# ['a', 'b', 't'] -> ['bat']
# ----------------------------------------------------------- #
