class Solution:
    def Sqrt(self, x: int) -> int:
        return int(x**0.5)

    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        res = 0
        while low <= high:
            mid = (low+high) // 2
            if mid**2 <= x:
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res
        