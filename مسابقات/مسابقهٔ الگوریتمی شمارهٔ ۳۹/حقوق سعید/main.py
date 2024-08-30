n, q = map(int, input().split())
sm = sum(map(lambda x: int(x) % (10 ** 9 + 7), input().split()))


for i in range(q):
    print((2 ** (int(input()) - n - 1) * sm) % (10 ** 9 + 7))
