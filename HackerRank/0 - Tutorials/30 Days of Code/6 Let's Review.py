n = int(input())
for i in range(n):    
    s = str(input())
    even_string = s[::2]
    odd_string = s[1::2]
    print(f"{even_string} {odd_string}")