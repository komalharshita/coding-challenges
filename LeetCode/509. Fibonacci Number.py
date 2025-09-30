class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            res = 0
        elif n == 1:
            res = 1
        else:
            a,b = 0,1
            for i in range(2, n+1):
                c = a+b
                a = b
                b = c
            res = b
        return res