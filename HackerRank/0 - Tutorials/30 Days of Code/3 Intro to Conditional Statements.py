if __name__ == '__main__':
    N = int(input().strip())


if N in range (1,101):
    if N % 2 != 0:
        print("Weird")
    elif N % 2 == 0 :
        if 2<= N <= 5:
            print("Not Weird")
        elif 6<= N <= 20:
            print("Weird")
        elif N > 20 :
            print("Not Weird")
    else:
        print("Weird")
