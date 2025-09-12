import math

def isprime(p):
    if p <= 1:
        return 'Not prime'
    if p <= 3:
        return 'Prime'
    if p % 2 == 0 or p % 3 == 0:
        return 'Not prime'
    i = 5
    while i * i <= p:
        if p % i == 0 or p % (i + 2) == 0:
            return 'Not prime'
        i += 6
    return 'Prime'

x = int(input())
for _ in range(x):
    p = int(input())
    print(isprime(p))