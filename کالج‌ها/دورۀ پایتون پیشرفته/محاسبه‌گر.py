def calculator(n, m, ls):
    new_list = list(map(sum, [ls[x:x+m] for x in range(0, n, m)]))
    val = sum(new_list[::2]) - sum(new_list[1::2])
    return val
