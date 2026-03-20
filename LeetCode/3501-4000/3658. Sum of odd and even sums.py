import math

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumodd = n ** 2
        sumeven = n * (n+1)
    
        res = math.gcd(sumodd, sumeven)
        return res
        