def friends_in_trouble(j_angry, s_angry):
    if (j_angry is True) and (s_angry is True):
        return True
    elif (j_angry is not True) and (s_angry is not True):
        return True
    else:
        return False