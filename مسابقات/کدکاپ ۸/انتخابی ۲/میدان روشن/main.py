t = int(input())


for _ in range(t):
    total_cost = 0
    last_selected = (0, 0)

    n = int(input())

    print(f'{n = }')

    cells = n * [0]

    costs = list(enumerate(map(int, input().split())))
    # costs.sort(key=lambda x: x[1])
    costs.sort(key=lambda x: -x[1] / (x[0]+1))

    for cost in costs:
        if cost[0] == last_selected[0] + 1:
            if n > 3:
                continue

        total_cost += cost[1]
        last_selected = cost

        cells[cost[0]] = 1
        cells[cost[0] - 1] = 1
        cells[(cost[0] + 1) % n] = 1

        if all(cells):
            break

    print(total_cost)
    print('--------------')
