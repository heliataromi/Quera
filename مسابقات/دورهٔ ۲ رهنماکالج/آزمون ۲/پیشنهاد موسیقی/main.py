u_name=[]
age=[]
city=[]
n=int(input())
albums=[]
m=0
name=''
for i in range(n):
    if(len(u_name)<=i):
        name=input().split()[-1]
    if(name not in u_name):
        u_name.append(name)
    age.append(int(input().split()[-1]))
    city.append(input().split()[-1])
    albums.append([])
    a=input()
    while(a[0]==' '):
        albums[i]+=a.split()[1:]
        a=input()
    else:
        if(i==n-1):
            m=int(a)
        else:
            name=a.split()[-1]
            u_name.append(name)
a_name=[]
singer=[]
genre=[]
tracks=[]
for i in range(m):
    a_name.append(input().split()[-1])
    singer.append(input().split()[-1])
    genre.append(input().split()[-1])
    tracks.append(int(input().split()[-1]))
q=int(input())
for i in range(q):
    quest=input().split()
    q_type=quest[0]
    ans=0
    if(q_type=='1'):
        u=quest[1]
        s=quest[2]
        if(u not in u_name or s not in singer):
            ans=0
        else:
            for x in albums[u_name.index(u)]:
                if(singer[a_name.index(x)]==s):
                    ans+=tracks[a_name.index(x)]
    if(q_type=='2'):
        u=quest[1]
        g=quest[2]
        if(u not in u_name or g not in genre):
            ans=0
        else:
            for x in albums[u_name.index(u)]:
                if(genre[a_name.index(x)]==g):
                    ans+=tracks[a_name.index(x)]
    if(q_type=='3'):
        a=int(quest[1])
        s=quest[2]
        if(a not in age or s not in singer):
            ans=0
        else:
            for j in range(len(age)):
                if(age[j]==a):
                    for x in albums[j]:
                        if(singer[a_name.index(x)]==s):
                            ans+=tracks[a_name.index(x)]
    if(q_type=='4'):
        a=int(quest[1])
        g=quest[2]
        if(a not in age or g not in genre):
            ans=0
        else:
            for j in range(len(age)):
                if(age[j]==a):
                    for x in albums[j]:
                        if(genre[a_name.index(x)]==g):
                            ans+=tracks[a_name.index(x)]
    if(q_type=='5'):
        c=quest[1]
        s=quest[2]
        if(c not in city or s not in singer):
            ans=0
        else:
            for j in range(len(city)):
                if(city[j]==c):
                    for x in albums[j]:
                        if(singer[a_name.index(x)]==s):
                            ans+=tracks[a_name.index(x)]
    if(q_type=='6'):
        c=quest[1]
        g=quest[2]
        if(c not in city or g not in genre):
            ans=0
        else:
            for j in range(len(city)):
                if(city[j]==c):
                    for x in albums[j]:
                        if(genre[a_name.index(x)]==g):
                            ans+=tracks[a_name.index(x)]
    print(ans)
