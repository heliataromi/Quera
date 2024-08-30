t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if not b.issubset(a):
        print('NO')

    else:
        #for x in 
        print('YES')
