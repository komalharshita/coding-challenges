def is_prime(n):
    if n <= 1:
        return False
    flag = True  

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            flag = False  
            break 
    
    return flag