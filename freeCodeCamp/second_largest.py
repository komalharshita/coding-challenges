def second_largest(arr):
    myset = set(arr)
    sorted_arr = list(myset)
    sorted_arr = sorted(sorted_arr)
    
    if len(sorted_arr) < 2:
        return None 
    
    return sorted_arr[-2] 