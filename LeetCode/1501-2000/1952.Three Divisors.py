class Solution:
    def isThree(self, n: int) -> bool:
        res = False
        root = int(n**0.5)
        if root * root == n:
            prime = True
            for i in range(2, int(root**0.5) + 1):
                if root % i == 0:
                    prime = False
                    break
            if prime and root > 1:
                res = True
        return res
        