from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        max_candies = max(candies)
        for c in candies:
            res.append(c + extraCandies >= max_candies)
        return res
        