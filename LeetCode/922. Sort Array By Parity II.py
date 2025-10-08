class Solution:
    def sortArrayByParityII(nums):
        i,j = 0,1
        n = len(nums)
        while i<n and j<n:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                nums[i],nums[j] = nums[j], nums[i]
        return nums