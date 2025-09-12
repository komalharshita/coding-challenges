import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    rev = arr[::-1]
    for i in rev: 
        print(i, end = " ")