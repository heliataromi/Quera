from math import sqrt

n = int(input())
summation = 0
number = 0

for i in range(1, n + 1):
	for j in range(1, int(sqrt(i)) + 1):
		if i % j == 0:
			summation += j
			number += 1

			if i // j != j:
				summation += i // j
				number += 1

print(number, summation)
