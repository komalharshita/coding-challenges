import math
import os
import random
import re
import sys
from statistics import median  

def quartiles(arr):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)  
    mid = n // 2
    
    if n % 2 == 0:
        low = sorted_arr[:mid]
        high = sorted_arr[mid:]
        q1 = int(median(low))
        q2 = int(median(sorted_arr))
        q3 = int(median(high))
    else:
        low = sorted_arr[:mid]
        high = sorted_arr[mid+1:]
        q1 = int(median(low))
        q2 = int(median(sorted_arr))
        q3 = int(median(high))
    
    return [q1, q2, q3] 