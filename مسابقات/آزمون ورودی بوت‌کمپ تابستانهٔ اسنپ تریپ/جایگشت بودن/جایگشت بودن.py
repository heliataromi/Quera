from collections import Counter
n, q = map(int, input().split())
numbers = list(map(int, input().split()))

for i in range(q):
	operation = input().split()
	if operation[0] == '+':
		idx = int(operation[1])
		val = int(operation[2])
		numbers[idx - 1] = val

	elif operation[0] == '?':
		l = int(operation[1])
		r = int(operation[2])
		temp = numbers[l - 1:r]
		lst = range(1, r - l + 2)
		if Counter(temp) == Counter(lst):
			print('YES')
		else:
			print('NO')
