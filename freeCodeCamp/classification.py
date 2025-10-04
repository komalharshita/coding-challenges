def classification(temp):
    if temp >= 30000:
        return "O"
    elif temp >= 10000 and temp <= 29999:
        return "B"
    elif temp >= 7500 and temp <= 9999:
        return "A"
    elif temp >= 6000 and temp <= 7499:
        return "F"
    elif temp >= 5200 and temp <= 5999:
        return "G"
    elif temp >= 3700 and temp <= 5199:
        return "K"
    elif temp >= 0 and temp <= 3699:
        return "M"
    else:
        return None





"""Space Week Day 1: Stellar Classification
October 4th marks the beginning of World Space Week. The next seven days will bring you astronomy-themed coding challenges.

For today's challenge, you are given the surface temperature of a star in Kelvin (K) and need to determine its stellar classification based on the following ranges:

"O": 30,000 K or higher

"B": 10,000 K - 29,999 K

"A": 7,500 K - 9,999 K

"F": 6,000 K - 7,499 K

"G": 5,200 K - 5,999 K

"K": 3,700 K - 5,199 K

"M": 0 K - 3,699 K

Return the classification of the given star."""