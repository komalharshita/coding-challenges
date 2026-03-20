class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n*(n+1) // 2
        left_sum = 0
        res = -1
        for i in range(1, n+1):
            left_sum = left_sum + i
            right_sum = total - left_sum + i
            if left_sum == right_sum:
                res = i
                break
        return res
        