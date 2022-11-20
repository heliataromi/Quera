class Piece:
	def __init__(self, name, state, cell):
		self.name = name
		self.state = state
		self. cell = cell


def get_dice():
	global k
	k += 1
	if k == 1:
		x.append(B)
	else:
		x.append((A * x[k - 2] + B) % m)

	return x[k - 1] % 6 + 1


def dice():
	if len(list(filter(lambda dice_result: dice_result != 6, dice_results))) != 0:
		return 'invalid dice rolling'

	temp = []
	out = get_dice()
	while out == 6:
		dice_results.append(out)
		temp.append(out)
		out = get_dice()

	dice_results.append(out)
	temp.append(out)
	return ' '.join(map(str, temp))


def enter(name):
	cells = []
	for piece in pieces:
		cells.append(piece.cell)

	for piece in pieces:
		if piece.name == name:
			if piece.state == 'in':
				return 'that is in'

			if 6 not in dice_results:
				return 'you need six'

			if 1 in cells:
				return 'busy starting cell'

			dice_results.remove(6)
			piece.cell = 1
			piece.state = 'in'
			return 1


def move(name, amount):
	cells = []
	for piece in pieces:
		cells.append(piece.cell)

	for piece in pieces:
		if piece.name == name:
			if amount not in dice_results:
				return 'invalid move'

			if piece.state == 'out':
				return 'it is not in'

			if 40 - piece.cell < amount:
				return 'you can not move'

			if piece.cell + amount in cells:
				return 'destination is busy'

			piece.cell += amount
			dice_results.remove(amount)
			return piece.cell


pieces = [Piece('R1', 'out', 0), Piece('R2', 'out', 0), Piece('R3', 'out', 0), Piece('R4', 'out', 0)]

dice_results = []

A, B, m = map(int, input().split())
k = 0
x = []
q = int(input())

for i in range(q):
	request = input().split()

	if request[0] == 'dice':
		print(dice())

	elif request[0] == 'enter':
		print(enter(request[1]))

	elif request[0] == 'move':
		print(move(request[1], int(request[2])))

	elif request[0] == 'giveup':
		dice_results.clear()
