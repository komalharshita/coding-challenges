class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = n
        count = 0
        while n>= 5:
            n //= 5
            count += n
        return count
        