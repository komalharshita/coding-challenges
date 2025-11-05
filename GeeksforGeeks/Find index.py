arr = tuple(map(int, input().split()))
x = int(input())

key = 0

for i in range(len(arr)):
    if arr[i] == x:
        key = i
        
print(key)