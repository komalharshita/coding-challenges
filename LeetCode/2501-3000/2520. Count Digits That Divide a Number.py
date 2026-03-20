class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        for d in str(num):
            digit = int(d)
            if digit != 0 and num % digit == 0 :
                count += 1
        return count