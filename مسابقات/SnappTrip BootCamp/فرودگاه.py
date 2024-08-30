class Plane:
	def __init__(self, id, status):
		self.id = id
		self.status = status

class Bound:
	def __init__(self, number, status, plane):
		self.number = number
		self.status = status
		self.plane = plane


def take_off(id):
	plane = None
	for p in planes:
		if p.id == id:
			plane = p

	if plane.status == 4:
		print('YOU ARE NOT HERE')

	elif plane.status == 3:
		print('YOU ARE LANDING NOW')

	elif plane.status == 2:
		print('YOU ARE TAKING OFF')

	elif plane.status == 1 and 'free' not in [bound.status for bound in bounds]:
		print('NO FREE BOUND')

	else:
		plane.status = 2
		for bound in bounds:
			if bound.status == 'free':
				bound.status = 'full'
				bound.plane = plane
				break
	return 1


def landing(id):
	plane = None
	for p in planes:
		if p.id == id:
			plane = p

	if plane.status == 1:
		print('YOU ARE HERE')

	elif plane.status == 2:
		print('YOU ARE TAKING OFF')

	elif plane.status == 3:
		print('YOU ARE LANDING NOW')

	elif plane.status == 4 and 'free' not in [bound.status for bound in bounds]:
		print('NO FREE BOUND')

	else:
		plane.status = 3
		for bound in reversed(bounds):
			if bound.status == 'free':
				bound.status = 'full'
				bound.plane = plane
				break
	return 1


def plane_status(id):
	plane = None
	for p in planes:
		if p.id == id:
			plane = p

	print(plane.status)
	return 1


def band_status(number):
	bound = None
	for b in bounds:
		if b.number == number:
			bound = b

	if bound.status == 'free':
		print('FREE')
	else:
		print(bound.plane.id)
	return 1


n, k = map(int, input().split())
planes = []
bounds = []
for i in range(n):
	planes.append(Plane(input(), 1))

for i in range(1, k + 1):
	bounds.append(Bound(i, 'free', ''))
q = int(input())

for i in range(q):
	operation = input().split()
	if operation[1] not in [plane.id for plane in planes]:
		planes.append(Plane(operation[1], 4))

	if operation[0] == 'TAKE-OFF':
		take_off(operation[1])

	elif operation[0] == 'LANDING':
		landing(operation[1])

	elif operation[0] == 'PLANE-STATUS':
		plane_status(operation[1])

	else:
		band_status(int(operation[1]))
