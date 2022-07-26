n = int(input())
x = 0
y = 0
if(n%2==0):
    if(n%4==0):
        x = n//4*(-1)
        y = n//4
    else:
        x = n//4 + 1
        y = n//4*(-1)
else:
    if((n-1)%4==0):
        x = (n-1)//4*(-1)
        y = x
    else:
        x = n//4 + 1
        y = x
print(x, y)
