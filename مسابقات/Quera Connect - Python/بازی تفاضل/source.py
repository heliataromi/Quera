def game(number):
	lst = list(str(number))
	lst.sort()
	return int(lst[1]) - int(lst[0])
