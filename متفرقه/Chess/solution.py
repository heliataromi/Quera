class Piece:
	def __init__(self, sort, color, position):
		self.sort = sort
		self.color = color
		self.position = position


class Board:

	def __init__(self):
		self.position = dict()
		self.position[(10, 10)] = Piece('K', 'black', (10, 10))
		self.position[(-10, -10)] = Piece('K', 'white', (-10, -10))

	def add(self, piece):
		if piece.position not in self.position and piece.sort != 'K':
			self.position[piece.position] = piece
		else:
			print("invalid query")

	def remove(self, position):
		if position in self.position.keys() and self.position[position].sort != 'K':
			self.position.pop(position)
		else:
			print("invalid query")

	def move(self, piece, position2):
		if piece in self.position.values():
			if list(self.position.keys())[list(self.position.values()).index(piece)] == piece.position:
				if position2 not in self.position.keys():
					self.position.pop(list(self.position.keys())[list(self.position.values()).index(piece)])
					self.position[position2] = piece
				else:
					if self.position[position2].sort != 'K' and self.position[position2].color != piece.color:
						self.position.pop(list(self.position.keys())[list(self.position.values()).index(piece)])
						self.position[position2] = piece
					else:
						print('invalid query')
			else:
				print('invalid query')
		else:
			print('invalid query')

	def is_mate(self, color):
		king = list(filter(lambda x: x.sort == 'K' and x.color == color, list(self.position.values())))[0]
		for piece in self.position.values():
			if king.position[0] - 1 <= piece.position[0] <= king.position[0] + 1:
				if king.position[1] - 1 <= piece.position[1] <= king.position[1] + 1:
					return True
			return False
