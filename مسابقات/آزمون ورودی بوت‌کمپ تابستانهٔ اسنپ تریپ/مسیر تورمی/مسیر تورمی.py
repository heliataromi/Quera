from math import comb

t = int(input())
for i in range(t):
	n = int(input())
	profits = []
	combs = 0
	for j in range(n // 2 + 2):
		combs += comb(n, j)
		profits.append(combs * 2 ** (n - j))
		if j != 0 and profits[j - 1] > profits[j]:
			print(j - 1)
			break
