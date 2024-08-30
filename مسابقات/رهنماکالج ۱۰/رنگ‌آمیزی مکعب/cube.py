def coloring(ls):
	for layer_index in range(len(ls)):
		if layer_index == 0 or layer_index == len(ls) - 1:
			for row_index in range(len(ls[layer_index])):
				for cube_index in range(len(ls[layer_index][row_index])):
					ls[layer_index][row_index][cube_index] = 1

		else:
			for row_index in range(len(ls[layer_index])):
				if row_index == 0 or row_index == len(ls[layer_index]) - 1:
					for cube_index in range(len(ls[layer_index][row_index])):
						ls[layer_index][row_index][cube_index] = 1

				else:
					for cube_index in range(len(ls[layer_index][row_index])):
						if cube_index == 0 or cube_index == len(ls[layer_index][row_index]) - 1:
							ls[layer_index][row_index][cube_index] = 1

						else:
							ls[layer_index][row_index][cube_index] = 0

	return ls


'''matrix = [
			[
				[1, 2, 3],
				[5, 5, 5],
				[5, 5, 5]
			],
			[
				[5, 5, 5],
				[5, 5, 5],
				[5, 5, 5]
			],
			[
				[5, 5, 5],
				[5, 5, 5],
				[5, 5, 5]
			]
		]

coloring(matrix)

for i in range(len(matrix)):
	print("{}th layer:".format(i+1))
	for j in matrix[i]:
		for k in j:
			print(k, end=' ')
		print()'''
