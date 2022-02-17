# Find the longest substring without repeating Characters.
def length_of_longest_substring(str2):
    substring = ''
    longest_substring = 0

    for char in str2:

        # Check if char is in current substring, if not add it
        if char not in substring:
            substring += char
        # Add string into the longest found substring
        else:
            substring = substring[substring.index(char) + 1:] + char
            print(substring)
            # Assign new or old maximum length to the longest substring
            longest_substring = max(longest_substring, len(substring))

    return longest_substring


if __name__ == '__main__':
    str1 = "abcabcbb"
    print("The input is : ", str1)

    total = length_of_longest_substring(str1)
    print("The longest substring without repeating Characters: ", total)

    """OUTPUT: 
    The input is :  abcabcbb
    bca
    cab
    abc
    cb
    b
    The longest substring without repeating Characters:  3
    """
