def quick_sort(numbers, low, high):
    if low >= high:
        return

    pivot_index = partition(numbers, low, high)
    quick_sort(numbers, low, pivot_index - 1)
    quick_sort(numbers, pivot_index + 1, high)


def partition(numbers, low, high):
    pivot_index = (low + high) // 2
    swap(numbers, pivot_index, high)

    i = low

    for j in range(low, high, 1):
        if numbers[j] <= numbers[high]:
            swap(numbers, i, j)
            i = i + 1

    swap(numbers, i, high)

    return i


def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


if __name__ == "__main__":
    nums = [-2, -1, 0, 1, 0, -1, -2]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
