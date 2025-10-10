arr = tuple(map(int, input().split()))

for a in arr:
    if(arr.count(a) > 1):
        print(False)
        break
else:
    print(True)