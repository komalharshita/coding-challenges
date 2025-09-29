class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num+1):
            digit_sum = 0
            for d in str(i):
                digit_sum = digit_sum + int(d)
            if digit_sum % 2 == 0:
                count += 1
        return count