def find_missing_numbers(arr):
    maxx = max(arr)
    whole = set(range(1, maxx+1))
    given = set(arr)
    missing = sorted(whole - given)
    return missing




""" Given an array of integers from 1 to n, inclusive, return an array of all the missing integers between 1 and n (where n is the largest number in the given array).

The given array may be unsorted and may contain duplicates.
The returned array should be in ascending order.
If no integers are missing, return an empty array.

"""