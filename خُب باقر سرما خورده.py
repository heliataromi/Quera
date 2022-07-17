from re import search

out = []
for i in range(5):
	inp = input()
	if search('HAFEZ', inp) or search('MOLANA', inp):
		out.append(i + 1)

if out:
	print(' '.join(map(str, out)))
else:
	print('NOT FOUND!')
