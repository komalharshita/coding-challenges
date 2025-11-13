from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort_nums = sorted(nums)
        rank = {}
        for i,num in enumerate(sort_nums):
            if num not in rank:
                rank[num] = i
        result = [rank[num] for num in nums]
        return result