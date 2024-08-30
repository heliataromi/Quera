n, s = input().split()
n = int(n)
s = set(s)
a = []
for i in range(n):
    a.append(input())
for x in a:
    y = set(x)
    if(y == s):
        print("Yes")
    else:
        print("No")
