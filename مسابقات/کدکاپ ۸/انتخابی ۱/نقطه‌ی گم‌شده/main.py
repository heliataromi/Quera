count_of_vertices = [{}, {}, {}]

for i in range(7):
    x, y, z = input().split()

    count_of_vertices[0][x] = count_of_vertices[0].get(x, 0) + 1
    count_of_vertices[1][y] = count_of_vertices[1].get(y, 0) + 1
    count_of_vertices[2][z] = count_of_vertices[2].get(z, 0) + 1

print(*[sorted(count_of_vertices[i].items(), key=lambda x: x[1])[0][0] for i in range(3)])
