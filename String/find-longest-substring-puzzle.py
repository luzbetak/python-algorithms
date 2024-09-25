# Function to find the length of the longest substring without repeating characters.
def length_of_longest_substring(str2):
    """
    Determines the length of the longest substring without repeating characters.
    Args:
        str2 (str): The input string in which to find the longest substring.
    Returns:
        int: The length of the longest substring without repeating characters.
    """

    substring = ''
    longest_substring = 0

    # Loop through each character in the input string
    for char in str2:

        # If the character is not in the current substring, add it to the substring
        if char not in substring:
            substring += char

        # If the character is already in the substring, adjust the substring
        # by removing characters up to and including the first occurrence of the repeating character
        else:
            # Update the substring to start just after the first occurrence of the repeating character
            substring = substring[substring.index(char) + 1:] + char

            # Update the longest_substring length if the current substring is longer
            longest_substring = max(longest_substring, len(substring))

    # After the loop, check once more to ensure the longest substring is correctly identified
    longest_substring = max(longest_substring, len(substring))

    return longest_substring


if __name__ == '__main__':
    # Example input string
    str1 = "abcabcbb"

    # Display the input string
    print("The input is : ", str1)

    # Calculate the length of the longest substring without repeating characters
    total = length_of_longest_substring(str1)

    # Display the result
    print("The longest substring without repeating characters: ", total)

    """
    Expected Output: 
    The input is :  abcabcbb
    bca
    cab
    abc
    cb
    b
    The longest substring without repeating characters:  3
    """
