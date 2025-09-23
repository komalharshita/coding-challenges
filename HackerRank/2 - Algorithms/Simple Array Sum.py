
def simpleArraySum(ar):
        sum = 0
        for i in ar:
                sum += i
        return sum


#to check if the code is correct 
arr = [ 433, 6645, 343234, 546543, 3567654]
ans = simpleArraySum(arr)
print(ans)