from itertools import combinations_with_replacement
n=int(input())
a=list(map(lambda x: int(x),input().split()))
b=list(combinations_with_replacement(a,2))
c=0
for x in b:
    c+=sum(range(x[0],x[1]+1))
print(c)
