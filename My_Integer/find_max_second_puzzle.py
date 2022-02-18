# Find largest and second-largest integer

my_list = [4, 2, 7, 9, 2]


def find_largest_integer():
    max1 = 0
    for i in my_list:
        if i > max1:
            max1 = i
    return max1


def find_second_largest_integer():
    max1 = sec = 0

    for i in my_list:
        if i > max1:
            if max1 > sec:
                sec = max1
            max1 = i
        elif i > sec:
            sec = i
    return sec


if __name__ == "__main__":
    print("Max: {}".format(find_largest_integer()))
    print("Sec: {}".format(find_second_largest_integer()))
