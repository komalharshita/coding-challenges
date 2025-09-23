def is_mirror(str1, str2):
    filter1 = ''.join(filter(str.isalpha, str1))
    filter2 = ''.join(filter(str.isalpha, str2))

    return filter1 == filter2[::-1]


"""
Given two strings, determine if the second string is a mirror of the first.

A string is considered a mirror if it contains the same letters in reverse order.
Treat uppercase and lowercase letters as distinct.
Ignore all non-alphabetical characters.
"""