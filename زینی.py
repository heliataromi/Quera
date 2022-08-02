n, m = map(int, input().split())
table = []
zini = 0

for i in range(n):
	table.append(list(map(int, input().split())))

for i in range(1, n - 1):
	for j in range(1, m - 1):
		if table[i][j - 1] > table[i][j] and table[i][j + 1] > table[i][j]:
			if table[i - 1][j] < table[i][j] and table[i + 1][j] < table[i][j]:
				zini += 1

		elif table[i][j - 1] < table[i][j] and table[i][j + 1] < table[i][j]:
			if table[i - 1][j] > table[i][j] and table[i + 1][j] > table[i][j]:
				zini += 1

print(zini)
