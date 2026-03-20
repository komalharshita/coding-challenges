class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n > 0 and (n & (n-1)) == 0 and (n-1) % 3 == 0:
            return True
        else:
            return False