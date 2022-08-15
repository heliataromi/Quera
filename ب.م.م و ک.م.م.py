def gcd(x, y):
	if y == 0:
		return x
	else:
		return gcd(y, x % y)


def lcm(a, b):
	t = a % b
	if t == 0:
		return a
	return a * lcm(b, t) // t


n, m = map(int, input().split())

print(gcd(n, m), lcm(n, m))
