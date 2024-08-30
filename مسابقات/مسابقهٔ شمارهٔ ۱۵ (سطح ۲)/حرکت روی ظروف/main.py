n = list(map(int, input().split()))
av = sum(n)/3
if(n[0] == n[1] == n[2]):
    print(0)
elif(av in n and n.count(av)==1):
    print(1)
else:
    print(2)
