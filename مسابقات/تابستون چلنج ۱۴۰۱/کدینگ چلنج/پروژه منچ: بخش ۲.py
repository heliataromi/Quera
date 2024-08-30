def get_dice():
	return x[k - 1] % 6 + 1


A, B, m = map(int, input().split())
n = int(input())

x = []
for k in range(1, n + 1):
	if k == 1:
		x.append(B)
	else:
		x.append((A * x[k - 2] + B) % m)


for k in range(1, n + 1):
	print(get_dice())
