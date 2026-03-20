class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = list(map(int, str(n)))
        total = 0
        for i in range(len(digits)):
            if i % 2 == 0:
                total = total + digits[i]
            else:
                total = total - digits[i]
        return total