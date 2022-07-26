m, s = map(int, input().split())
a = []
lst = []
for i in range(10**(m-1), 10**m):
    lst = list(str(i))
    if(sum(list(map(int, lst))) == s):
        a.append(i)
        break
if(a):
    lst.sort(reverse = True)
    a.append(''.join(lst))
    print(a[0], a[1])
else:
    print(-1, -1)
