def mid(string):
    if len(string) % 2 == 0:
        return ""  
    else:
        middle_index = len(string) // 2
        return string[middle_index]