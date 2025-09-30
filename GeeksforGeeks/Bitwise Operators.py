a=int(input())
b=int(input())
c=int(input())

d= a ^ a
e= c ^ b
f= a & b
g= c | ( a ^ a)
e= ~e
print(d, e, f, g)