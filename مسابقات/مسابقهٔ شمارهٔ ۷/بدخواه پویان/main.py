p, d = map(int, input().split())
x = 1

while True:
	if 0 <= (d * x) % p <= p // 2:
		print(d * x)
		break
	else:
		x += 1
