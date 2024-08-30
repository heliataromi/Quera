n, v = map(int, input().split())
juices = []
happiness = 0

for i in range(n):
    juices.append(tuple(map(int, input().split())))

juices.sort(key=lambda x: -x[0] / x[1])

for h_i, v_i in juices:
    if v == 0:
        break

    if v >= v_i:
        happiness += h_i
        v -= v_i

    else:
        happiness += v / v_i * h_i
        v -= v

print(f'{happiness:.1f}')
