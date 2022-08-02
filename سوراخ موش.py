x1, x2 = map(int, input().split())

if x1 == x2:
	print('Saal Noo Mobarak!')


else:
	if x2 > x1:
		print((x2 - x1) * 'R')
	elif x1 > x2:
		print((x1 - x2) * 'L')
