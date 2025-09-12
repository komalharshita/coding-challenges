class Solution:
    def checkStatus(self, a, b, flag):
        if ( a>= 0) ^ (b>=0) and not flag:
            return True
        if ( a< 0) and ( b< 0) and flag:
            return True
        return False