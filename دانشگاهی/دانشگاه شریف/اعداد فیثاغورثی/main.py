a=[]
for i in range(3):
    a.append(int(input()))
a.sort()
if(a[0]**2+a[1]**2==a[2]**2):
    print('YES')
else:
    print('NO')
