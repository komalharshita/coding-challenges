from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = sorted(p[0] for p in points)
        max_gap = 0
        for i in range(1,len(x)):
            max_gap = max(max_gap, x[i] - x[i-1])
        return max_gap
        