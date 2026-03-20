from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low , high = 0, len(arr)
        while low < high:
            mid = (low+high) // 2
            if arr[mid] - (mid+1) < k:
                low = mid + 1
            else:
                high = mid
        return (low+k)
        