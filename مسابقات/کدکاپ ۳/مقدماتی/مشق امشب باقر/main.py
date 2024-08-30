a=list(map(lambda x: int(x),input().split()))
if(sum(a)==180 and 0 not in a):
    print('Yes')
else:
    print('No')
