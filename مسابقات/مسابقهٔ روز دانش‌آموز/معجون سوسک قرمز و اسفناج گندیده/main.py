a, b, c, d, m = map(int, input().split())

next_a = a + m * c
next_b = b + m * d

if next_a > next_b:
	if next_a - a > next_b - b:
		print('Eyval baba!')

	else:
		print('Naaa, eshtebahe!')

if next_b > next_a:
	if next_b - b > next_a - a:
		print('Eyval baba!')

	else:
		print('Naaa, eshtebahe!')
