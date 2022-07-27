from math import sqrt


def is_prime(n):
	for i in range(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False

	return True


a = int(input())
b = int(input())
primes = []

for i in range(a + 1, b):
	if is_prime(i):
		primes.append(i)

print(','.join(map(str, primes)))
