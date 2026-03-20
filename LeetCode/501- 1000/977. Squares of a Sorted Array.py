class Solution:
    def sortedSquares(nums):
        l = 0
        n = len(nums)
        r = pos = n-1
        res = [0]*n
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[pos] = nums[l]**2
                l+=1
            else:
                res[pos] = nums[r]**2
                r -=1
            pos -=1
        return res


        