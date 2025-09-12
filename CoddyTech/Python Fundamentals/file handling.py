
import os

a = open("test.txt", "r")

file = open("data.txt", "r")

print(file.readline())

file = open("yourfile.txt", "w")
file.write("Hello World!")

os.remove("data.txt")

