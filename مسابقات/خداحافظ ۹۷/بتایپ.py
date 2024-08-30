s=input()
a=list(s)
b=0
c=''
d=0
for i in range(a.count('=')):
    b=a.index('=')
    a.remove('=')
    if(b!=0):
        del a[b-1]
    if(b==0):
        d+=1
for x in a:
    c+=x
print(d*'='+c)
