class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp, suffixSum = initializeDP(n, stoneValue)
        for i in range(n - 1, -1, -1):
            dp[i] = computeOptimalChoice(i, n, stoneValue, suffixSum, dp)
        return determineWinner(dp[0])


def initializeDP(n, stoneValue):
    dp = [0] * (n + 1)                          # FIX: implement dp array
    suffixSum = [0] * (n + 1)                   # FIX: implement suffix sum array
    for i in range(n - 1, -1, -1):
        suffixSum[i] = suffixSum[i + 1] + stoneValue[i]
    return dp, suffixSum                         # FIX: return both arrays


def computeOptimalChoice(i, n, stoneValue, suffixSum, dp):
    best = float('-inf')                         # FIX: implement choice logic
    for k in range(1, 4):
        if i + k <= n:
            advantage = suffixSum[i] - suffixSum[i + k] - dp[i + k]
            if advantage > best:
                best = advantage
    return best                                  # FIX: return computed best


def determineWinner(aliceAdvantage):
    if aliceAdvantage > 0:                       # FIX: implement winner check
        return "Alice"
    elif aliceAdvantage < 0:
        return "Bob"
    else:
        return "Tie"