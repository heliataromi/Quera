print(*sorted(set([int(x) for x in input().split()[5::6] if int(x)%6==0])))
