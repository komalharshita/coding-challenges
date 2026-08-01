class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [nums[i] for i in range(n)]

        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                pick_left = nums[left] - dp[left + 1]
                pick_right = nums[right] - dp[left]

                dp[left] = max(pick_left, pick_right)

        return dp[0] >= 0