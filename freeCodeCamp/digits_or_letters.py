def digits_or_letters(s):
    digits = '0123456789' 
    letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'  
    nod = []  
    nol = []  
    res = ""

    for i in range(len(s)):  
        if s[i] in digits:
            nod.append(s[i])
        elif s[i] in letters:
            nol.append(s[i])

    if len(nod) > len(nol):
        res = "digits"
    elif len(nol) > len(nod):
        res = "letters"
    else:
        res = "tie"

    return res

"""
Given a string, return "digits" if the string has more digits than letters, 
"letters" if it has more letters than digits, 
and "tie" if it has the same amount of digits and letters.
Digits consist of 0-9.
Letters consist of a-z in upper or lower case.
Ignore any other characters.
"""