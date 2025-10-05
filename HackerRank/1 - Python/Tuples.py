#run using python 2

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    s = tuple(integer_list)
    print(hash(s))