n, m = map(int, input().split())
a = []
trips = []
cost = 0

for i in range(n):
	a.append(tuple(map(int, input().split())))

for i in range(m):
	trips.append(tuple(map(int, input().split())))

for trip in trips:
	cost += a[trip[0] - 1][trip[1] - 1]

print(cost)
