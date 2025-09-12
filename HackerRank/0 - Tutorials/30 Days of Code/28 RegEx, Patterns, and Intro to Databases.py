import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    res = []
    pattern = re.compile(r'@gmail.com$')
    for _ in range(N):
        firstName, emailID = input().strip().split()
        if pattern.search(emailID):
            res.append(firstName)
    
    for x in sorted(res):
        print(x)