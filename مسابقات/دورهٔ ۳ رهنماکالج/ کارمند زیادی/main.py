d=dict()
for i in range(int(input())):
    name=input().split()[0]
    if name not in d:
        d[name]=1
    else:
        d[name]+=1
a=1
for k,v in d.items():
    if(v>a):
        a=v
print(a)
