class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=abs)
        n = len(nums)
        neg_count = n // 2
        
        # Subtract squares of the smallest elements (odd positions)
        # Add squares of the largest elements (even positions)
        result = 0
        for i in range(neg_count):
            result -= nums[i] ** 2
        for i in range(neg_count, n):
            result += nums[i] ** 2
        
        return result