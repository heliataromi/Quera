n=input()
a=0
while(len(n)>1):
    a=0
    for x in n:
        a+=int(x)
    n=str(a)
print(n)
