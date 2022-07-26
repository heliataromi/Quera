def lcm(a, b, ans = 0): 
    m = max([a, b])
    for i in range(m, a * b + 1):
        if(i % a == 0 and i % b == 0):
            ans = i
            break
    return(ans)
a, b = map(int, input().split())
print(int(lcm(a, b)/b))
