# -------------------------------------------------- #
def two_sum(nums, sum_target):
    my_set = {}
    for pos, value in enumerate(nums):
        reminder = sum_target - value
        if reminder in my_set:
            return [my_set[reminder], pos]
        my_set[value] = pos
    return []


# -------------------------------------------------- #
# O(n2)
# Result: [1, 4] = 3 + 2 = 5
# -------------------------------------------------- #
result = two_sum([8, 3, 6, 1, 2, 4], 5)
print(result)
