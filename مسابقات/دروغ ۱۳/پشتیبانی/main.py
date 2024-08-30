from itertools import permutations



def triangle(s):
    perms = permutations(s, 3)
    for perm in perms:
        a, b, c = perm[0], perm[1], perm[2]
        if a + b > c and b + c > a and a + c >b:
            return("YES")

    return("NO")

s = list(map(int, input().split()))
print(triangle(s))
