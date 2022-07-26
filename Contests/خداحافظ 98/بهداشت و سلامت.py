x = int(input())
n = int(input())
if(n == 0):
    print(20)
elif(n == 7):
    print(x)
else:
    print(x - n if x - n >= 0 else 0)
