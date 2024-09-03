def find_indices(list_to_check, item_to_find):
	return [idx for idx, value in enumerate(list_to_check) if value == item_to_find]


t = int(input())

for _ in range(t):
	n, k = map(int, input().split())
	if k != 0:
		wall = [n * [''], n * ['']]
		for i in range(k):
			r, c = input().split()
			c = int(c)
			if r == 'u':
				wall[0][c - 1] = '*'
			if r == 'd':
				wall[1][c - 1] = '*'
		print(wall)
		outlets = [[], []]
		first_indices = find_indices(wall[0], '*')
		print(first_indices)
		for i in range(len(first_indices)):
			if i == 0:
				outlets[0].append((0, first_indices[i]))
				outlets[0].append((first_indices[i], first_indices[i + 1]))
			if i == len(first_indices) - 1:
				outlets[0].append((first_indices[i], n - 1))
			else:
				outlets[0].append((first_indices[i], first_indices[i + 1]))
		print(outlets)


	else:
		print(1)