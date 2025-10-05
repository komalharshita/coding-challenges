if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    
new_list = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n ]
print(new_list)
