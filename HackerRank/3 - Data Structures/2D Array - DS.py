def hourglassSum(arr):
        n,m = len(arr) , len(arr[0])
        flag = None
        for i in range(n-2):
                for j in range(m-2):
                        s = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
                        if flag is None or s > flag:
                                flag = s
        return flag
        return max(s)