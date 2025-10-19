class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n + (n %2)
        while left <= right:
            mid = (left+right) // 2
            if (isBadVersion(mid)) == True:
                right = mid - 1
            else:
                left = mid + 1
        return left