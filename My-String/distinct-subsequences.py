def distinct_subsequences(str2, set2):
    if len(str2) == 0:
        return

    if str2 not in set2:
        set2.add(str2)

        # Traverse current string, one by one remove every character.
        for char in range(len(str2)):
            t = list(str2).copy()
            t.remove(str2[char])
            t = ''.join(t)
            distinct_subsequences(set2, t)

    return


if __name__ == "__main__":

    str1 = "abcd"
    set1 = set()
    distinct_subsequences(str1, set1)

    for i in sorted(set1):
        print(i)

""" OUTPUT:
a
ab
abc
abcd
abd
ac
acd
ad
b
bc
bcd
bd
c
cd
d
"""