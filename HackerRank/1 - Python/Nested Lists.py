if __name__ == '__main__':
    list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([name, score])
    marks = [ i[1] for i in list ]
    scl = sorted(set(marks))[1]
    names = sorted([i[0] for i in list if i[1] == scl])
    
    for name in names:
        print(name)