class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        result = []
        for i in range(1, 1001):
            if a % i == 0 and b % i == 0:
                result.append(i)
        return len(result)