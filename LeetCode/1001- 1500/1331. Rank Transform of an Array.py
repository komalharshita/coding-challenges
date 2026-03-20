from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {num: i+1 for i, num in enumerate(sorted(set(arr)))}
        res = [ranks[num] for num in arr ]
        return res 
        