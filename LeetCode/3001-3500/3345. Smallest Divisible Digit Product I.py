class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # Scan from n upward; within 10 steps a number ending in 0 guarantees a match
        for candidate in range(n, n + 10):
            # Compute the product of all digits
            product = 1
            for ch in str(candidate):
                product *= int(ch)
            # Return the first candidate whose digit product is divisible by t
            if product % t == 0:
                return candidate