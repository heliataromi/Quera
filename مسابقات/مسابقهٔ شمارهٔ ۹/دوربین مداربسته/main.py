xs = []
ys = []
x, y = 0, 0

for i in range(3):
	coordinate = list(map(int, input().split()))
	xs.append(coordinate[0])
	ys.append(coordinate[1])

for xx in xs:
	if xs.count(xx) == 1:
		x = xx

for yy in ys:
	if ys.count(yy) == 1:
		y = yy

print(x, y)
