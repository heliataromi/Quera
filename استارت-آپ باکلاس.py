chocolates = list(map(int, input().split()))
people = [0] * 4

i = 0
while True:
	chocolates[i % 4] -= 1
	people[i % 4] += 1
	chocolates = chocolates[1:] + chocolates[0:1]
	i += 1
	if 0 in chocolates:
		break

print(' '.join(map(str, people)))
