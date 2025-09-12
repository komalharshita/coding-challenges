n = int(input().strip())
phonebook = {}

for _ in range(n):
    name, number = input().strip().split()
    phonebook[name.lower()] = int(number)

try:
    while True:
        search_name = input().strip()
        key = search_name.lower()
        if key in phonebook:
            print(f"{search_name}={phonebook[key]}")
        else:
            print("Not found")
except EOFError:
    pass