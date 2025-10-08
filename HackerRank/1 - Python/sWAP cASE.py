def swap_case(s):
        res = ''
        for char in s:
                if char.islower():
                        res += char.upper()
                elif char.isupper():
                        res += char.lower()
                else:
                        res += char
        return res