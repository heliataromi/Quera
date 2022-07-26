a, b, l = map(int, input().split())
ans = 0
for i in range(l):
    if(i%2==0):
        ans += a
    else:
        ans += b
print(ans)
