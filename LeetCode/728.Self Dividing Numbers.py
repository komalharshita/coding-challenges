from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right+1):
            temp = num
            ok = True
            for d in str(num):
                digit = int(d)
                if digit == 0 or num % digit != 0:
                    ok = False
                    break
            if ok:
                ans.append(num)
        return ans
        