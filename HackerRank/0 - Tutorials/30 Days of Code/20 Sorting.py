import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    swap = 0
    for i in range (n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                swap += 1
                a[j], a[j+1] = a[j+1], a[j]
    print(f'Array is sorted in {swap} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')