def count_substring(string, sub_string):
        sub = len(sub_string)
        c = 0
    
        for i in range(len(string) - sub + 1):
                if string[i:i + sub] == sub_string:
                        c += 1
            
        return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)