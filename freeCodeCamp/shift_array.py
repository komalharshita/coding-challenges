def shift_array(arr, n):
    n = n % len(arr)
    result = []
    for i in range(len(arr)):
        result.append(arr[(i + n) % len(arr)])
    return result