n, k = map(int, input().split())

c = []
for i in range(n):
    c.append(int(input().split()))

if k <= sum(c):
    print('YES')
else:
    print('NO')
