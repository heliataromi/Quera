def factorial(n):
    if(n == 1):
        return(n)
    else:
        return(n * factorial(n - 1))
a = str(factorial(int(input())))
ans = '0'
c = 1
while(ans == '0'):
    ans = a[-c]
    c += 1
print(ans)
