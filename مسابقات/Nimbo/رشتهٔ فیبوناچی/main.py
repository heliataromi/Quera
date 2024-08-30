# def fibonacci(x):
# 	if x == 1:
# 		return 1
#
# 	elif x == 2:
# 		return 2
#
# 	else:
# 		return fibonacci(x - 1) + fibonacci(x - 2)

fibs = [1, 2]

n = int(input())
out = []

for i in range(1, n + 1):
	fibs.append(fibs[i] + fibs[i - 1])

for i in range(1, n+1):
	if i in fibs:
		out.append('+')
	else:
		out.append('-')

print(''.join(out))

