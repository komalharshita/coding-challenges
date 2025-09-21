s1 = 'GfG'  # single quote
s2 = "GfG"  # double quote
print(s1)
print(s2)

s = """I am Learning
Python String on GeeksforGeeks"""
print(s)

s = '''I'm a 
Geek'''
print(s)

s = "GeeksforGeeks"
print(s[0])   # first character
print(s[4])   # 5th character

s = "GeeksforGeeks"
print(s[-10])   # 3rd character
print(s[-5])    # 5th character from end

s = "GeeksforGeeks"
print(s[1:4])    # characters from index 1 to 3
print(s[:3])     # from start to index 2
print(s[3:])     # from index 3 to end
print(s[::-1])   # reverse string

s = "Python"
for char in s:
    print(char)

s = "geeksforGeeks"
s = "G" + s[1:]   # create new string
print(s)

s = "GfG"
del s

s = "hello geeks"
s1 = "H" + s[1:]                   # update first character
s2 = s.replace("geeks", "GeeksforGeeks")  # replace word
print(s1)
print(s2)

s = "GeeksforGeeks"
print(len(s))

s = "Hello World"
print(s.upper())
print(s.lower())

s = "   Gfg   "
print(s.strip())    

s = "Python is fun"
print(s.replace("fun", "awesome"))

s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

s = "Hello "
print(s * 3)

name = "Alice"
age = 22
print(f"Name: {name}, Age: {age}")

s = "My name is {} and I am {} years old.".format("Alice", 22)
print(s)

s = "GeeksforGeeks"
print("Geeks" in s)
print("GfG" in s)

