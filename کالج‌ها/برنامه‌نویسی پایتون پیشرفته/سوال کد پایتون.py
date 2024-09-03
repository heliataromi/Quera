def solve(address):
    f = open(address,'r')
    read = f.readlines()
    read = list(map(lambda x: x[:-1], read))
    print(read)
    ans = len(read)
    for x in read:
        y = x.strip()
        print(y)
        if(y == ''):
            ans -= 1
        else:
            if(all([i==' ' for i in x[:len(x)-1]])):
                ans -= 1
            if(y[0] == '#'):
                 ans -= 1
    return(ans)
