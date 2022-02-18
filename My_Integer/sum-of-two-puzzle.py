# -------------------------------------------------- #
def two_sum(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        remaining = target - v
        if remaining in seen:
            return [seen[remaining], i]
        seen[v] = i
    return []


# -------------------------------------------------- #
# O(n2)
# Result: [1, 4] = 3 + 2 = 5
# -------------------------------------------------- #
result = two_sum([8, 3, 6, 1, 2, 4], 5)
print(result)
