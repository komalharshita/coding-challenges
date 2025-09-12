if __name__ == '__main__':
    a = []
    for _ in range(6):
        a.append(list(map(int, input().rstrip().split())))
    row=len(a)
    R=[]
    for i in range(row-2):
        for j in range(row-2):
            R.append(a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2])
    print(max(R))