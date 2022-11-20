t = int(input())
for _ in range(t):
    n, s, a = map(int, input().split())
    if ((s - a) % n == 0) and (a < s):
        print((s - a) // n)
    else:
        print(-1)
