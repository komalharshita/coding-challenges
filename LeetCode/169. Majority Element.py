class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sortnums = sorted(nums)
        n = len(sortnums) // 2
        return sortnums[n]
        