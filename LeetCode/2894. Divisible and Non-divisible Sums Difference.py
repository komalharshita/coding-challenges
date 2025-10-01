class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n*(n+1) // 2
        divisible = 0

        for i in range(m, n+1, m):
            divisible = divisible + i
            
        non_div = total - divisible

        return non_div - divisible
        