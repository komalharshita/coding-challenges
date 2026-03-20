from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        n = len(arr)
        while i+1 < n and arr[i]<arr[i+1]:
            i+= 1
        if i == 0 or i == n-1:
            return False
        else:
            while i+1 < n and arr[i] > arr[i+1]:
                i+= 1
        return i == n-1
        