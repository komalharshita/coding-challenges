if __name__ == '__main__':
    N = int(input())
    
mylist = []

for i in range(N):
    
    index = [i for i in input().split()]
    
    if index[0] == "insert":
        mylist.insert(int(index[1]),int(index[2]))
    elif index[0] == "print":
        print(mylist)
    elif index[0] == "remove":
        mylist.remove(int(index[1]))
    elif index[0] == "append":
        mylist.append(int(index[1]))
    elif index[0] == "sort":
        mylist.sort()
    elif index[0] == "pop":
        mylist.pop()
    elif index[0] == "reverse":
        mylist.reverse()
