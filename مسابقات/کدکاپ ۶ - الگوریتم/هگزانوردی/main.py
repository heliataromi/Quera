def find_path(x, y):
    if y == 1 or y == -1:
        return abs(x)
    if x == 0:
        return abs(y)
    return find_path(x, y - 1) + find_path(x - 1, y)


t = int(input())
paths = {'A': (1, 0), 'B': (0, 1), 'C': (0, 1), 'D': (-1, 0), 'E': (0, -1), 'F': (0, -1)}

for _ in range(t):
    gasht = input()
    coordinate = [0, 0]
    for path in gasht:
        coordinate[0] += paths[path][0]
        coordinate[1] += paths[path][1]

    print(find_path(coordinate[0], coordinate[1]))
