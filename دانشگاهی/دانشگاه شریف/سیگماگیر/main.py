n = int(input())
m = int(input())
sigma = 0

for i in range(-10, m + 1):
	temp = 0

	for j in range(1, n + 1):
		temp += (i + j) ** 3 / j ** 2

	sigma += temp

print(int(sigma))
