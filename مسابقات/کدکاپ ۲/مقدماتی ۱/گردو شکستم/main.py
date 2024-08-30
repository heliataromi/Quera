from math import gcd

n, x, y = map(int, input().split())

if n % gcd(x, y) != 0:
	print(-1)

else:
	pass
