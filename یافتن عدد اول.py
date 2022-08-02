from math import sqrt


def is_prime(x):
	for i in range(2, int(sqrt(x)) + 1):
		if x % i == 0:
			return False

	return True


n = int(input())
b = sum(list(map(int, list(str(n)))))

k = n + 1
numbers = 0

while True:
	if is_prime(k):
		numbers += 1

		if numbers == b:
			print(k)
			break

	k += 1
