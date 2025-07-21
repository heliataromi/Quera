def coloring(cube: list[list[list[int]]]) -> None:
	for layer_index in range(len(cube)):
		if layer_index == 0 or layer_index == len(cube) - 1:
			for row_index in range(len(cube[layer_index])):
				for cube_index in range(len(cube[layer_index][row_index])):
					cube[layer_index][row_index][cube_index] = 1

		else:
			for row_index in range(len(cube[layer_index])):
				if row_index == 0 or row_index == len(cube[layer_index]) - 1:
					for cube_index in range(len(cube[layer_index][row_index])):
						cube[layer_index][row_index][cube_index] = 1

				else:
					for cube_index in range(len(cube[layer_index][row_index])):
						if cube_index == 0 or cube_index == len(cube[layer_index][row_index]) - 1:
							cube[layer_index][row_index][cube_index] = 1

						else:
							cube[layer_index][row_index][cube_index] = 0

	return cube
