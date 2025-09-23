
def compareTriplets(a, b):
        alice = 0
        bob = 0
        for i in range(0, 3):
                if a[i] > b[i]:
                        alice += 1
                elif a[i] < b[i]:
                        bob += 1
                        
        res = [alice, bob]
        return res


#to check if the code is correct 
t1 = [3,5,2]
t2 = [5,7,2]
ans = compareTriplets(t1, t2)
print(ans)