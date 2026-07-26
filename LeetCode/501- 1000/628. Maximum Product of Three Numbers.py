from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Initialize top-3 max and bottom-2 min trackers
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')

        for num in nums:
            # Inline top-three update to avoid per-iteration function call overhead
            if num > max1:
                max3, max2, max1 = max2, max1, num
            elif num > max2:
                max3, max2 = max2, num
            elif num > max3:
                max3 = num

            # Inline bottom-two update
            if num < min1:
                min2, min1 = min1, num
            elif num < min2:
                min2 = num

        # Two candidates: three largest, or two most-negative × largest
        return max(max1 * max2 * max3, min1 * min2 * max1)