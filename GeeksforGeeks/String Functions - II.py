def gfg(S):
    b = S.lower()
    if (b.startswith('gfg') and b.endswith('gfg')):
        print("Yes")
    elif (b.startswith('GFG') and b.endswith('GFG')):
        print("Yes")
    elif (b.startswith('gfg') and b.endswith('GFG')):
        print("Yes")
    elif (b.startswith('GFG') and b.endswith('gfg')):
        print("Yes")
    else:
        print("No")