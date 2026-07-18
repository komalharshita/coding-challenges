from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_gcd = max(nums)

        # dp[g1][g2] = number of ways to partition processed elements
        # g1=0 means seq1 is empty, g2=0 means seq2 is empty
        dp = [[0] * (max_gcd + 1) for _ in range(max_gcd + 1)]
        dp[0][0] = 1

        for num in nums:
            new_dp = [[0] * (max_gcd + 1) for _ in range(max_gcd + 1)]
            for g1 in range(max_gcd + 1):
                for g2 in range(max_gcd + 1):
                    if dp[g1][g2] == 0:
                        continue
                    val = dp[g1][g2]

                    # Choice 1: Skip this number
                    new_dp[g1][g2] = (new_dp[g1][g2] + val) % MOD

                    # Choice 2: Add to seq1
                    ng1 = self.computeNewGcd(g1, num)
                    new_dp[ng1][g2] = (new_dp[ng1][g2] + val) % MOD

                    # Choice 3: Add to seq2
                    ng2 = self.computeNewGcd(g2, num)
                    new_dp[g1][ng2] = (new_dp[g1][ng2] + val) % MOD

            dp = new_dp

        return self.countMatchingGcdPairs(dp, max_gcd, MOD)

    def computeNewGcd(self, current_gcd: int, num: int) -> int:
        if current_gcd == 0:
            return num
        return gcd(current_gcd, num)

    def countMatchingGcdPairs(self, dp: List[List[int]], max_gcd: int, mod: int) -> int:
        ans = 0
        for g in range(1, max_gcd + 1):
            ans = (ans + dp[g][g]) % mod
        return ans