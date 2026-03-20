from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums) 
        inc = all(nums[i] <= nums[i+1] for i in range(n-1))
        dec = all(nums[i] >= nums[i+1] for i in range(n-1))
        return dec or inc