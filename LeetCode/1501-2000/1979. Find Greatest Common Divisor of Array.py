from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_val = findMinimum(nums)
        max_val = findMaximum(nums)
        return computeGCD(min_val, max_val)


def findMinimum(nums):
    min_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val


def findMaximum(nums):
    max_val = nums[0]
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val


def computeGCD(a, b):
    while b:
        a, b = b, a % b
    return a