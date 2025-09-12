def recur(n):
    if n == 0:
        return
    print(n)
    recur(n-1) 

def sum_all(n):
    if n == 0:
        return 0
    return n + sum_all(n-1)

def recurs(n):
    if n == 0:
        return 1
    return n * recurs(n-1)