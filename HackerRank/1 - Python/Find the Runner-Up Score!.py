if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    if 2 <= n <= 10 and all(-100 <= score <= 100 for score in arr):
        highest = max(arr)
        arr = [x for x in arr if x != highest]
        runner_up = max(arr)
        print(runner_up)
