from typing import List

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        lsum = 0
        for i in range(len(nums)):
            if lsum == total - lsum - nums[i]:
                return i
                break
            lsum += nums[i]
        return -1