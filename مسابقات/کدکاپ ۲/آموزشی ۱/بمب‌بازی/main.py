n,m=map(int,input().split())
mp=[]
for i in range(n):
    mp.append([])
    for j in range(m):
        mp[i].append(0)
bomb_n=int(input())
for i in range(bomb_n):
    x,y=map(lambda z: int(z)-1,input().split())
    mp[x][y]='*'
    if(x>0 and type(mp[x-1][y])==int):
        mp[x-1][y]+=1
    if(x<n-1 and type(mp[x+1][y])==int):
        mp[x+1][y]+=1
    if(y>0 and type(mp[x][y-1])==int):
        mp[x][y-1]+=1
    if(y<m-1 and type(mp[x][y+1])==int):
        mp[x][y+1]+=1
    if(y>0 and x>0 and type(mp[x-1][y-1])==int):
        mp[x-1][y-1]+=1
    if(y<m-1 and x<n-1 and type(mp[x+1][y+1])==int):
        mp[x+1][y+1]+=1
    if(x<n-1 and y>0 and type(mp[x+1][y-1])==int):
        mp[x+1][y-1]+=1
    if(x>0 and y<m-1 and type(mp[x-1][y+1])==int):
        mp[x-1][y+1]+=1
for x in mp:
    print(' '.join(list(map(str,x))))
