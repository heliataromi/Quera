n, t = input().split()
n = int(n)

for i in range(n):
    code = input()

    if set(code) == set(t):
        print('Yes')

    else:
        print('No')
