class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s = 1
        i = 2
        while i*i <= num:
            if num % i == 0:
                s = s+i
                if i != num//i :
                    s = s + (num//i)
            i = i + 1
        if s == num and num != 1:
            return True 
        else:
            return False 