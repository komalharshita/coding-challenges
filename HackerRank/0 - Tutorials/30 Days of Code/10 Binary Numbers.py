n = int(input())

binary = bin(n)[2:]

count = 0
max_count = 0

for digit in binary:
    if digit == '1':
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0
    

print(max_count)