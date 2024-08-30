a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = "no"
if(a[0] >= b[0] and a[1] >= b[1]):
    ans = "yes"
print(ans)
