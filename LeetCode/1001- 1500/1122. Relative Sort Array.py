from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = { num: i for i, num in enumerate(arr2)}
        result = sorted(arr1, key = lambda x:order.get(x, x+1000))

        return result
        