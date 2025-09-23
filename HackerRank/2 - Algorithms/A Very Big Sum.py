def aVeryBigSum(ar):
    longg = 0
    for i in ar:
        longg += i
    return longg

#to check if the code is correct 

arr = [2,4,6,2,4,6,3]
res = aVeryBigSum(arr)
print(res)