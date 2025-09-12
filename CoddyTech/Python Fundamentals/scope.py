b = 200
def f():
    a = 300
    print(a)
f()
print(b)

def fun():
    global c
    c = 300
fun()
print(c)