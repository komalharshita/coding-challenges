import os


def diagonalDifference(arr):
        n = len(arr)
        primary = secondary = 0
        
        for i in range(n):
                primary += arr[i][i]
                secondary += arr[i][n-1-i]
                
        return abs(primary - secondary)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
