def blood_validator(d, m, c):
	d_and_m = set(list(d + m))
	for x in c:
		if x != 'O' and x != '-':
			if x not in d_and_m:
				return 'invalid'
	return 'valid'


t = int(input())

for _ in range(t):
	d, m, c = input().split()
	print(blood_validator(d, m, c))
