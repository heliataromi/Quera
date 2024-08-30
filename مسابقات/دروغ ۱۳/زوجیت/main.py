def zojOrFard(n):
    if n % 2 == 0:
        return("fard")
    else:
        for i in range(1, n):
            if n % i == 0 and i != 1:
                return("fard")
        return("zoj")


n = int(input())
print(zojOrFard(n))
