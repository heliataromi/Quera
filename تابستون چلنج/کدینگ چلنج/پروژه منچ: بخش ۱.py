d = int(input())

rows = []
for i in range(5):
	rows.append([])
	for j in range(5):
		rows[i].append('.')

if d % 2 != 0:
	rows[2][2] = 'o'

if d >= 2:
	rows[1][3] = 'o'
	rows[3][1] = 'o'

if d >= 4:
	rows[1][1] = 'o'
	rows[3][3] = 'o'

if d == 6:
	rows[2][1] = 'o'
	rows[2][3] = 'o'

for row in rows:
	print(''.join(row))
