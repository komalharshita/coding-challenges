class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p, s = 1, 0
        while n > 0:
            digit = n % 10
            p *= digit
            s += digit
            n //= 10
        return p - s