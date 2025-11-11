def count(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    consonant_count = 0
    
    for char in s:
        if char.isalpha(): 
            if char.lower() in vowels: 
                vowel_count += 1
            else:  
                consonant_count += 1

    return [vowel_count, consonant_count]



"""
Vowels and Consonants
Given a string, return an array with the number of vowels and number of consonants in the string.

Vowels consist of a, e, i, o, u in any case.
Consonants consist of all other letters in any case.
Ignore any non-letter characters.
For example, given "Hello World", return [3, 7].
"""