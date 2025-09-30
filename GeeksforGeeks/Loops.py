def multiplicationTable(n):
    for i in range(1, 11):
        print(f"{n*i}", end = " ")

n = 4
for i in range(0, n):
    print(i)

li = ["geeks", "for", "geeks"]
for i in li:
    print(i)
    
tup = ("geeks", "for", "geeks")
for i in tup:
    print(i)
    
s = "Geeks"
for i in s:
    print(i)
    
d = dict({'x':123, 'y':354})
for i in d:
    print("%s  %d" % (i, d[i]))
    
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),

li = ["geeks", "for", "geeks"]
for index in range(len(li)):
    print(li[index])

li = ["geeks", "for", "geeks"]
for index in range(len(li)):
    print(li[index])
else:
    print("Inside Else Block")

cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")

cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")
else:
    print("In Else Block")

from __future__ import print_function
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)

fruits = ["apple", "orange", "kiwi"]
iter_obj = iter(fruits)
while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break