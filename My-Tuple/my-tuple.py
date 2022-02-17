import random


# ----------------------------------------------------------------------#
def find_element():
    my_tuple = ("kevin", "thomas", "luzbetak")
    print("All =", my_tuple)
    print("First two", my_tuple[:2])

    if "luzbetak" in my_tuple:
        print("luzbetak is in the tupple ")

    print(random.choice(my_tuple))  # print random element


# ----------------------------------------------------------------------#
if __name__ == "__main__":
    find_element()
