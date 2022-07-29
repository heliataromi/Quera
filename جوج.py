def road_check(n, road):
	for i in range(n):
		if i != 0 or i != n - 1:
			if road[i] > road[i - 1] and road[i] > road[i + 1]:
				return 'Ey baba :('

	return 'Bah Bah! Ajab jooji!'


n = int(input())
road = list(map(int, input().split()))

print(road_check(n, road))
