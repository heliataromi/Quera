class Foo:
	x = 0

	def __setattr__(self, name, value):
		if value >= 0:
			self.__dict__[name] = int(str(value)[len(str(value)) - 2:])
		else:
			self.__dict__[name] = -1
