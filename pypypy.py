def get_max(n) :
    mx = 0
    for i in range(n):
        b = int(input())
        if mx < b :
            mx = b
    return(mx)
n = int(input("Enter integer n : "))
print(get_max(n))
        
        
