def selection_sort(numbers):
    for i in range(len(numbers) - 1):

        index = i

        for j in range(i + 1, len(numbers), 1):
            if numbers[j] < numbers[index]:
                index = j

        if index != i:
            swap(numbers, index, i)
    return numbers


def swap(numbers, i, j):
    temp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = temp


if __name__ == "__main__":
    nums = [-1, 4, 5, 2, -2, 0, 1, 2, 3, 2, 1, 0, 1, 2, 3]
    print(selection_sort(nums))
