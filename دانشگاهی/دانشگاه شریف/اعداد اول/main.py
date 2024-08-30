def is_prime(n):
	if n == 1:
		return False
	else:
		for i in range(2, n):
			if n % i == 0:
				return False

	return True


a = int(input())
b = int(input())

for j in range(a, b + 1):
	if is_prime(j):
		print(j)
