x, y = map(int, input().split())

for i in range(7, 1, -1):
	if i != x or i != y:
		print(1)
		print(i, i)
		break
