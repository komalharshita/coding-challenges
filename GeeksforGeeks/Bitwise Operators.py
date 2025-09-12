a=int(input())
b=int(input())
c=int(input())
#code here
#Do a^a below
d= a ^ a
#Do c^b below
e= c ^ b
#Do a&b below
f= a & b
#Do c|(a^a) below
g= c | ( a ^ a)
#Do ~e below
e= ~e
print(d, e, f, g)