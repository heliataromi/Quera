from math import log2, gcd

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if n % k == 0:
        print(0)

    elif (x := log2(k / gcd(n, k))).is_integer():
        print(int(x))

    else:
        print(-1)
