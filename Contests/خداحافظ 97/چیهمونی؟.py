n=int(input())
a=[]
for i in range(n):
    a.append(input())
h=0
m=0
for x in a:
    if(x[-1]=='+'):
        if(int(x[-7:-5])>h):
            m=int(x[-4:-2])
            h=int(x[-7:-5])
        elif(int(x[-7:-5])==h):
            if(int(x[-4:-2])>m):
                m=int(x[-4:-2])
    if(x[-1]=='-'):
        if(int(x[-7:-5])<h):
            m=int(x[-4:-2])
            h=int(x[-7:-5])
        elif(int(x[-7:-5])==h):
            if(int(x[-4:-2])>m):
                m=int(x[-4:-2])
h=str(h)
m=str(m+1)
if(len(h)==1):
    h='0'+h
if(len(m)==1):
    m='0'+m
print(h+':'+m)
