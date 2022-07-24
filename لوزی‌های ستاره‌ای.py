n = int(input())

for i in range(n // 2 + 1):
	print(((n // 2 - i) * ' ' + (1 + 2 * i) * '*' + (n // 2 - i) * ' ') * 2)

for i in range(n // 2):
	print(((i + 1) * ' ' + (n - 2 * i - 2) * '*' + (i + 1) * ' ') * 2)
