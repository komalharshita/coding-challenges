class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]  # dp[i][j] = max relative score for subarray piles[i..j]
        
        for i in range(n):
            dp[i][i] = piles[i]
        
        for length in range(2, n + 1):  # Build solutions for increasing subarray lengths
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])  # Pick left or right, subtract opponent's best
        
        return dp[0][n - 1] > 0  # Alice wins if her relative score is positive