t = int(input())

while t > 0:
    n = int(input())
    s = input()
    res = ''
    
    for i in range(0, n, 2):
        if s[i] == '0' and s[i + 1] == '0':
            res += 'A'
        elif s[i] == '0' and s[i + 1] == '1':
            res += 'T'
        elif s[i] == '1' and s[i + 1] == '0':
            res += 'C'
        elif s[i] == '1' and s[i + 1] == '1':
            res += 'G'
    
    print(res)
    t -= 1
