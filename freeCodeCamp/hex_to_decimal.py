def hex_to_decimal(hexx):
    hc = { '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, 
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E':14, 'F': 15 }
    res = 0
    hexx = hexx.upper()
    for i in range(len(hexx)):
        res += hc[hexx[i]] * (16 ** (len(hexx) - 1 - i))
    return res


"""
Given a string representing a hexadecimal number (base 16), return its decimal (base 10) value as an integer.

Hexadecimal is a number system that uses 16 digits:

0-9 represent values 0 through 9.
A-F represent values 10 through 15.
"""